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
    if lists:
        new.append[lists[0][0]]
    i = 0
    g = 0
    while (i < lists[i]):
        f = 0
        while (f < len(lists[i])):
            new.append[lists[i][f]]
            #  Aqui reiniciar la lista para las comprobaciones desde 0 cada vez que se agrega algo????
            if (new[g] < new[g - 1]):
                temp = new[g - 1]
                new[g - 1] = new[g]
                new[g] = temp
            f += 1
            g += 1


if __name__ == "__main__":

    # ------------ TESTS FOR py_constellation_mapper -----------------------
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
