def find_number_pairs(numbers, N=10):
    result = []
    for x in numbers:
        for y in numbers:
           if x != y:
               if x + y == N and (y,x) not in result:
                   result.append((x,y))
    return result

class ABC:
    pass

if __name__ == '__main__':
    input_list = [9,1,3,8,7]
    print(find_number_pairs(input_list))

