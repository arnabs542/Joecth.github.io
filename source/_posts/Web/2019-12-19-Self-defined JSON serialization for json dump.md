---

layout: post
categories: Web
tag: [] 

---

date: 2019-12-21
----


###  Self-defined serializable for JSON dump



```python
class MySerialization(json.JSONEncoder):
    def foo(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, time):
            return obj.__str__()
        else:
            return super(NpEncoder, self).default(obj)
```


Then, 

```python
json.dumps(data, cls=MySerialization) 
```





![image-20200103161320526](https://tva1.sinaimg.cn/large/006tNbRwgy1gajfy4hc41j30m405jn01.jpg)





```python
    def make_art_inf(self, cfg):
        info = {}
        d1 = {
                "name": os.path.basename(cfg['path']),  
                "config_json": cfg, 	# This should be a json configuration
            }

        info["manuscript"] = json.dumps(d1)   # should do json.dumps() here instead of at line 5
        return info


```

