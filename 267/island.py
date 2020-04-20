# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


def get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total numbe)
    """
    nums = 0
    n_rows = len(map_)
    n_cols = len(map_[0])
    
    # Determine the number of borders of this field that do not connect
    # to another field of the map. 

    # 1 1 0
    # 0 0 0
    # 0 0 0
    # -->
    #(0,0) left top bottom
    #(0,1) top bottom right
    # Sums up to 6

    # 0 1 0
    # 1 1 1
    # 0 1 0
    # -->
    # (0,1) top left right
    # (1,0) top left bottom
    # (1,1) -
    # (1,2) top right bottom
    # (2,1) left right bottom
    # Sums up to 12j
    if map_[r][c]==0:
        return 0
    if r == 0:
        nums += 1 # Top always
    if r == n_rows-1:
        nums += 1 # Bottom always
    if c == 0:
        nums += 1 # Left always
    if c == n_cols - 1:
        nums += 1
    if r-1 >= 0 and map_[r-1][c]==0:
        nums += 1
    if r+1 < n_rows and map_[r+1][c]==0:
        nums += 1
    if c-1 >= 0 and map_[r][c-1]==0:
        nums += 1
    if c+1 < n_cols and map_[r][c+1]==0:
        nums += 1
    #print(f"({r},{c}): {nums}")
    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    # your code here
    for r in range(len(map_)):
        for c in range(len(map_[0])):
            perimeter += get_others(map_, r, c)
    return perimeter

if __name__ == "__main__":
    map1 = [[1,1,1,1],
            [1,0,0,0],
            [1,0,0,0],
            [1,0,0,0],
            [1,1,1,1]]
    print(island_size(map1))
