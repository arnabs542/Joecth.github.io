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