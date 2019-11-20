def binary_search(sequence, target):
    return binary_search_r(sequence, target, 0, len(sequence) - 1)

def binary_search_nr(sequence, target):
    l = 0
    r = len(sequence) - 1

    while l <= r:
        m = (l+r)//2 
        if sequence[m] < target:
            l = m + 1
        elif sequence[m] > target:
            r = m - 1
        else:
            return m
    return None

def binary_search_r(sequence, target, l, r):
    print(f"sequence: {sequence} target: {target} l:{l} r{r}")
    if l > r: return None
    m = (l+r)//2
    if sequence[m] < target:
        return binary_search_r(sequence, target, m+1,r)
    elif sequence[m] > target:
        return binary_search_r(sequence, target, l, m -1)
    return m

if __name__ == "__main__":
    from test_binary_search import PRIMES
    print(binary_search(PRIMES,5))


