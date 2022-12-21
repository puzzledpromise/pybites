import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    iterables = []

    for it in args:
        if not it:
            continue
        it = [i for i in it if i is not None]
        iterables.append(it)
    print(iterables)
    if not iterables:
        return set()
    if len(iterables) == 1:
        if iterables[0] is None:
            return set()
        return set(iterables[0])
    
    
    
    result = functools.reduce(lambda x, y: set(x) & set(y), iterables)
    return result

if __name__ == '__main__':
    print(intersection((None, )))
        
