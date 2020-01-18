class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __getitem__(self, key):
        return dict.__getitem__(self,key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delitem__(self, key):
        print(f"delitem got called with the key {key}!")
        if key in self:
            print(f"Going to delete {key} from this object.")
            return dict.__delitem__(self, key)
        else:
            print(f"Could not find {key}!")

    def __delattr__(self, name):
        return dict.__delitem__(self,name)
