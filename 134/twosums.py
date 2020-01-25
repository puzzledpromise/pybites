def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    numbers_sort_idxd = sorted([(n,i) for i,n in enumerate(numbers)])
    for n1,i1 in numbers_sort_idxd:
        for n2,i2 in numbers_sort_idxd:
            if n1 == n2:
                continue
            elif n1 + n2 > target:
                break
            else:
                if n1 + n2 == target:
                    return (i1, i2)
    return None


if __name__ == '__main__':
    numbers = [3, 10, 14, 8, 15, 5, 16, 13, 9, 2]
    target = 30
    result = two_sums(numbers, target)
    print(result)
