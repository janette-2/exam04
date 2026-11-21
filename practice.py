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
    n = len(s)
    dp = [0] + [999999999999999999999999999] * n
    for end in range(1, n + 1):
        for start in range(end):
            substring = s[start:end]
            if substring == substring[::-1]:
                if start == 0:
                    cuts = 0
                else:
                    cuts = dp[end - 1] + 1
                dp[end] = min(dp[end], cuts)
    return dp[n]


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    parents = {}
    for package in packages:
        parents[package] = []
    for parent in parents:
        for package, dependency in packages.items():
            if package in packages:
                if parent in dependency:
                    parents[parent].append(package)
    # print(f"Parents :{parents}")

    remains = {}
    for package in packages:
        remains[package] = 0
    for package in remains:
        for key, dependency in packages.items():
            if key == package:
                for item in dependency:
                    if item in packages:
                        remains[package] += 1
    # print(f"Remains :{remains}")

    queue = []
    for package, remain in remains.items():
        if remain == 0:
            queue.append(package)
    # print(f"Queue Init: {queue}")

    result = []
    while queue:
        # guardar el item en result y quitarlo de queue
        processing = queue.pop(0)
        result.append(processing)
        # recorrer cada uno de los hijos del item a procesar
        for son in parents[processing]:
            # buscar el item a procesar en su entrada de remains
            # restarle -1 a estos items
            if remains[son] > 0:
                remains[son] -= 1
        # los que hayan quedado en remains == 0, añadirlos a queue
        for son in parents[processing]:
            if remains[son] == 0:
                queue.append(son)
    return result


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
    print("-------------py_palindrome_partitioner---------------")
    print(palindrome_partitioner("aab"))
    print(palindrome_partitioner("aba"))
    print(palindrome_partitioner("abc"))
    print("----------------------------------------------------")
    print()
    print()
    print("-------------py_package_dependency_resolver----------")
    print(package_dependency_resolver({"app": ["database"], "database":
                                      ["driver"], "driver": []}))
    print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))
    print(package_dependency_resolver({}))
    print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))
    print(package_dependency_resolver({"web": [], "api": [], "frontend":
                                       ["web"], "backend": ["api"]}))
