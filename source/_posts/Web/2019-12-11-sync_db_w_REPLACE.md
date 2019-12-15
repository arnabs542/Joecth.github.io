---
layout: post
categories: Web
tag: [] 




---

### Sync DB w/ REPLACE


```python
import requests
import json
from requests.auth import HTTPBasicAuth
import glob
import os
import re
import argparse

class ConfJsonHandler(object):
    def __init__(self, conf_json_root):
        self.conf_json_root = conf_json_root
        self.serv_b = ServB()

    def upload_one_style_w_replace(self, style='ZZZ'):
        '''
        Example Below:
        '''
        # obj.serv_b.post_filtering(filter_pat)       # 根据 filter_pat 拿data跟id
        # obj.serv_b.delete_by_filtering(filter_pat)  # 根据 filter_pat 找到的data的id作软删除
        # obj.serv_b.get_all_materials({'material_type': 'template', 'content.template':'测试测试'})

        # style = 'ZZZ'
        local_style = self.style_mapper(style)  # 'ZZZ' --> '测试测试'

        upload = True  # TODO: Set to True to upload to mongodb
        filter_del = {
            "filter": {'material_type': 'template', 'content.template': local_style}}  # E.g. content.template: '光'
        # filter_del = {"filter":{'content.template':'aaa'}}
        self.run_one_style(style, upload, filter_del)

        filter_pat = filter_del
        res = self.serv_b.post_filtering(filter_pat)
        if 200 != res.status_code:
            raise Exception("FAILED in upload_one_style_w_replace.")


    def style_mapper(self, style):
        if style == 'A':
            local_style = 'AAA'
        elif style == 'B':
            local_style = 'BBB'
        elif style == 'C':
            local_style = 'CCC'
        elif style == 'D':
            local_style = 'DDD'
        elif style == 'G':
            local_style = 'EEE'
        elif style == 'M':
            local_style = 'FFF'
        # elif style == 'E':
        #     local_style = 'GGG'
        elif style == 'ZZZ':
            local_style = 'ZZZZZZZ'
        else:
            raise Exception("{} has no corresponding chinese style".format(style))
        return local_style

    def run_post(self):
        styles_paths = glob.glob(os.path.join(self.conf_json_root, '*'))
        for s in styles_paths:      # [A, B, C]
            style = s.split('/')[-1]
            self.run_one_style(style)

    def run_one_style(self, style, upload, filter_del):
        # self.serv_b.set_filter_del(filter_del)

        scs_paths = glob.glob(os.path.join(self.conf_json_root, style, '*'))
        for s in scs_paths:         # ['out_jsons/A/3_4_detail_res2_sc4',
                                    # 'out_jsons/A/3_4_detail_res2_sc3',
                                    # 'out_jsons/A/3_4_detail_res2_sc2', ,...]
            print()
            print('-'*20, 'Processing {}'.format(s), '-'*20)
            sc = s.split('/')[-1]
            self.run_one_sc(style, sc, upload, filter_del)

    def run_one_sc(self, style, sc, upload, filter_del):
        conf_path = glob.glob(os.path.join(self.conf_json_root, style, sc, '*'))[0]
                                    # out_jsons/A/3_4_detail_res2_sc3/3_4_detail_res2_sc3.json
        basename = os.path.basename(conf_path)
                                    # 3_4_detail_res2_sc3.json
        basename_split = basename.split('.')[0].split('_')
        scale = basename_split[0] + ':' + basename_split[1]     # 3_4 --> 3:4
        intent = basename_split[2]  # detail
        img = basename_split[-3]    # img2 TODO: use re to support number > 10
        vid = basename_split[-2]   # vid0
        sc = basename_split[-1]    # sc3
        with open(conf_path, 'r+') as f:
            conf = json.load(f)

        '''
        Info for payload 
        '''
        id = conf_path
        template = self.style_mapper(style)
        pic_num = int("".join(re.findall(r"\d+", img)))
        vid_num = int("".join(re.findall(r"\d+", vid)))
        config = conf
        stage = self.intent_mapper(intent)
        style = sc
        scale = scale

        payload = self.pkg_payload(id=id, template=template, pic_num=pic_num, vid_num = vid_num, config=config, stage=stage, style=style, scale=scale)
        # payload = {"bbb":55, "ccc":999}
        # payload = config
        # exit()
        print('payload to upload: {}'.format(payload))

        if filter_del:
            self.serv_b.delete_by_filtering(filter_del)

        # TODO: set upload to True if going to upload
        if upload:
            self.serv_b.post(payload)

    def intent_mapper(self, intent):
        ###

        return d.get(intent, '')

    def pkg_payload(self, id:int, template:str, pic_num:int, vid_num:int, config:json, stage:list, style:str, scale:str) -> None:
        print('in pkg_payload')
        payload = {
            "id":id,
            "template":template,
            "pic_num":pic_num,
            "vid_num":vid_num,
            "config":config,
            "stage":stage,
            "style":style,
            "scale":scale
        }

        return payload


class ServB(object):
    def __init__(self, account='', pw=''):

        self.account = 'serv_b-admin'
        self.pw = 'passwd'
        self.filter_del = None
        # self.account = 'user@xxxxxxxxxxxxx.com'
        # if not pw:
        #     fname = 'password.txt'
        #     with open(fname, 'r+') as f:
        #         pw = f.readline().strip()
        #         self.pw = pw
        # else:
        #     self.pw = pw

    def set_filter_del(self, filter_del=None):
        self.filter_del = filter_del

    def post(self, payload):
        print("=== In POST ALL ===")
        # POST
        # payload = {"bbb":55, "ccc":88}
        res = "/api/v3/add/materials"
        res = requests.post("https://serv_b2.xxxxxxxxxxxxx.com"+res, auth=HTTPBasicAuth(self.account, self.pw),
                        json={"material_content":payload, "material_type":"template"})
        print(res.status_code)
        print(json.dumps(res.json(), ensure_ascii=False))

    def post_one_testing_data(self):
        # POST
        payload = {"bbb":55, "ccc":88}
        res = "/api/v3/add/materials"
        res = requests.post("https://serv_b2.xxxxxxxxxxxxx.com"+res, auth=HTTPBasicAuth(self.account, self.pw),
                            json={"material_content":payload, "material_type":"helloworld"})
        print(res.status_code)
        print(json.dumps(res.json(), ensure_ascii=False))

    def put(self, payload, id):
        # PUT
        res = "/api/v3/dp_materials"
        res = requests.post("https://serv_b2.xxxxxxxxxxxxx.com"+res, auth=HTTPBasicAuth(self.account, self.pw),
                            json={"content":payload})
        print(res.status_code)
        print(json.dumps(res.json(), ensure_ascii=False))

    def put_one_by_id(self, payload, id='c42f7c9aaf01463f88b01d46e7d0b850'):
        # PUT
        payload = {"bbb":55, "ccc":7777}
        res = "/api/v3/dp_materials/" + str(id)
        res = requests.put("https://serv_b2.xxxxxxxxxxxxx.com"+res, auth=HTTPBasicAuth(self.account, self.pw),
                            json={"content":payload})
        print(res.status_code)
        print(json.dumps(res.json()))

    def post_filtering(self, filter):
        print("In POST_FILTERING()")
        res = "/api/v3/search/dp_materials"
        try:
            res = requests.post("https://serv_b2.xxxxxxxxxxxxx.com"+res, auth=HTTPBasicAuth(self.account, self.pw),
                           json=filter)
        except Exception as e:
            raise Exception("Invalid filter for post: {}".format(filter))
        print(res.status_code)
        # print(res.text)
        print('post filtering: {}'.format(json.dumps(res.json(), ensure_ascii=False)))
        return res

    def delete_by_id(self, id='f18c4278016643e7b84815279dbef12f'):
        res = "/api/v3/dp_materials/" + str(id)
        res = requests.delete("https://serv_b2.xxxxxxxxxxxxx.com"+res, auth=HTTPBasicAuth(self.account, self.pw))
        print(res.status_code)
        print(json.dumps(res.json(), ensure_ascii=False))


    def get_all_materials(self, filter):
        res = "/api/v3/dp_materials"
        res = requests.get("https://serv_b2.xxxxxxxxxxxxx.com"+res, auth=HTTPBasicAuth(self.account, self.pw),
                            # json=filter)
                           params=filter)
        print(res.status_code)
        # print(res.text)
        print(json.dumps(res.json(), ensure_ascii=False))

    def delete_by_filtering(self, filter):
        print("In DELETE_BY_FILTERING()")
        res = self.post_filtering(filter)
        if res.status_code != 200:
            raise Exception("Faid filtering existing data to Delete..")

        count = res.json().get('count', 0)
        data = res.json().get('data', {})
        assert(count == len(data))
        if 0 == count:
            print('No data to be deleted..')

        ids = []
        for item in data:
            ids.append(item.get('material_id', 0))

        for id in ids:
            self.delete_by_id(id)



if __name__ == '__main__':
    run_all = False
    print('='*40)
    conf_json_root = 'out_jsons'    # TODO: use argumentParse
    # conf_json_root = 'trans_jsons'    # TODO: use argumentParse

    obj = ConfJsonHandler(conf_json_root)
    if run_all:
        obj.run_post()

    # obj.serv_b.post_one_testing_data()
    # obj.serv_b.put_one_testing_data({"bbb":53335, "ccc":666})   # replace existing data w/ a new one

    obj.upload_one_style_w_replace('ZZZ')
    '''
    Example Below:
    '''
    # obj.serv_b.post_filtering(filter_pat)       # 根据 filter_pat 拿data跟id
    # obj.serv_b.delete_by_filtering(filter_pat)  # 根据 filter_pat 找到的data的id作软删除
    # obj.serv_b.get_all_materials({'material_type': 'template', 'content.template':'测试测试'})

    # style = 'ZZZ'
    # local_style = obj.style_mapper(style)  # 'ZZZ' --> '测试测试'
    #
    # upload = True  # TODO: Set to True to upload to mongodb
    # filter_del = {
    #     "filter": {'material_type': 'template', 'content.template': local_style}}  # E.g. content.template: '光'
    # obj.run_one_style(style, upload, filter_del)
    #
    # filter_pat = filter_del
    # res = obj.serv_b.post_filtering(filter_pat)

    # TODO: query by content.config.path
    # obj.serv_b.delete_by_id()

```

