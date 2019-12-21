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

然后在调用json.dump/dumps时，指定使用自定义序列化方法



```python
json.dumps(data, cls=MySerialization) 
```