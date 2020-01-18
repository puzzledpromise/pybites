class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """
    def __keytransform__(self, key):
         return key
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v
            
        
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)
    
    
    def __setattr__(self, key, value):
        self[key] = value

    def __getitem__(self, key):
        return dict.__getitem__(self, self.__keytransform__(key))
        
    def __delitem__(self, key):
        return dict.__delitem__(self, self.__keytransform__(key))



     

if __name__ == '__main__':
    d = JsObject(a=1, b=2, c=3)
    d.d = 4
    print(len(d))
    print(list(d.keys()))