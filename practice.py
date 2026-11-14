def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    res = []
    i = 0
    while (i < dim):
        res = res + ['.' * dim]
        i = i + 1
    for coor in stars:
        coor_x, coor_y = coor
        if (coor_x < dim and coor_y < dim):
            temp = list(res[coor_x])
            temp[coor_y] = "*"
            res[coor_x] = "".join(temp)
    return res


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    intersections = []
    found = False
    if not lists:
        return []
    for item in lists[0]:
        i = 1
        while (i < len(lists)):
            if item in lists[i]:
                found = True
                i += 1
            else:
                found = False
                break
        if found or len(lists) == 1:
            intersections.append(item)
    return list(set(intersections))


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    new = []
    i = 0
    while (i < len(lists)):
        f = 0
        while (f < len(lists[i])):
            new.append(lists[i][f])
            new = keep_ordering(new)
            f += 1
        i += 1
    return new


# AUX DE MERGE_SORTED_LISTS
def keep_ordering(new: list[int]) -> list[int]:
    i = len(new) - 1
    last = new[i]
    temp = new[i - 1]
    while (last < temp and i > 0):
        new[i - 1] = last
        new[i] = temp
        i -= 1
        last = new[i]
        temp = new[i - 1]
    return new


def palindrome_partitioner(s: str) -> int:
    back = len(s) - 1
    front = 0
    partitions = 0
    while (back != 0 or front != len(s)):
        if (s[front] != s[back]):
            front = 0
            back -= 1
            partitions += 1
        else:
            res = is_palindrome(s[:back + 1])
            if res:
                # Separar la parte que resta del palindromo y volver a analizar ese cacho.
    return partitions


def is_palindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1
    while(start != end or end > 0 or start < len(s)):
        if (s[start] == s[end]):
            start += 1
            end -= 1
        else:
            break
    if (start == end):
        return True
    return False


if __name__ == "__main__":

    print("-------------py_constellation_mapper------------")
    print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
    print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
    print(constellation_mapper([], 2))
    print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
    print(constellation_mapper([(0, 0), (5, 5)], 3))
    print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))
    print("---------------------------------------------------")
    print()
    print()
    print("-------------py_list_intersection_finder------------")
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
    # breakpoint()
    print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
    print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
    print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
    print(list_intersection_finder([]))
    print(list_intersection_finder([[1, 2, 3], []]))
    print(list_intersection_finder([[5]]))
    print("----------------------------------------------------")
    print()
    print()
    print("-------------py_merge_sorted_lists---------------")
    print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
    print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
    print(merge_sorted_lists([[5], [1, 3], [2, 4]]))
    print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))
    print(merge_sorted_lists([[], [1, 2, 3]]))
    print(merge_sorted_lists([[]]))
    print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))
    print(merge_sorted_lists([[10], [10], [10]]))
    print("----------------------------------------------------")
    print()
    print()
