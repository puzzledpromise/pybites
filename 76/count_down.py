from functools import singledispatch
from datetime import datetime


@singledispatch
def count_down(data_type):
    if not isinstance(data_type, str):
        raise ValueError()
    values = list(data_type)
    while(len(values)>0):
        print("".join(values))
        values.pop()


@count_down.register(int)
def _(data_type: int):
    count_down(str(data_type))

@count_down.register(set)
def _(data_type:set):
    count_down("".join([str(x) for x in data_type]))

@count_down.register(tuple)
def _(data_type:tuple):
    count_down("".join([str(x) for x in data_type]))
    
@count_down.register(float)
def _(data_type:float):
    count_down(str(data_type))


@count_down.register(dict)
def _(data_type:dict):
    count_down([str(k) for k, v in data_type.items()])

@count_down.register(list)
def _(data_type):
    count_down("".join([str(d) for d in data_type]))

@count_down.register(range)
def _(data_type):
    count_down("".join([str(d) for d in data_type]))

if __name__ == '__main__':
    data_type = {1: 'a', 2: 'b', 3: 'c'}
    data_type = {'1','2','3','4'}
    count_down(data_type)
    print(type(range(5)))
