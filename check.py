def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> None:
    # list[str]:
    res = []
    for i in range(dim):
        res.append([])
    for i in range(dim):
        res[i] = "." * dim
    # print(res)
    for coord in stars:
        coord_x, coord_y = coord
        if coord_x > dim or coord_y > dim:
            continue
        temp = res[coord_x]
        temp = list(temp)
        temp[coord_y] = '*'
        res[coord_x] = ''.join(temp)
    # print(res)
    return res


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    common = []
    flag = True
    if not lists:
        return []
    for num in lists[0]:
        for left in lists[1:]:
            if num in left:
                flag = True
            else:
                flag = False
                break
        if flag:
            common.append(num)
    return list(set(common))


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    res = []
    for list in lists:
        for num in list:
            res.append(num)
            res = keep_ordering(res)
    return res


def keep_ordering(ref: list[int]) -> list[int]:
    i = len(ref) - 1
    l_ref = ref
    prev = i - 1
    while i > 0 and prev >= 0:
        if l_ref[i] < l_ref[prev]:
            temp = l_ref[prev]
            l_ref[prev] = l_ref[i]
            l_ref[i] = temp
        i -= 1
        prev -= 1
    return l_ref


if __name__ == "__main__":
    print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
    print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
    print(merge_sorted_lists([[5], [1, 3], [2, 4]]))
    print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))
    print(merge_sorted_lists([[], [1, 2, 3]]))
    print(merge_sorted_lists([[]]))
    print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))
    print(merge_sorted_lists([[10], [10], [10]]))
