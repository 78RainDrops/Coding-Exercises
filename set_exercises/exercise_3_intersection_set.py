set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


def intersection_with_for_loop(set1, set2):
    intersec_set = set()

    for item in set1:
        if item in set2:
            intersec_set.add(item)

    return intersec_set


def using_intersection_func(set1, set2):
    num_set = set1.intersection(set2)
    return num_set


def using_ampersand(set1, set2):
    num_set = set1 & set2
    return num_set


print(using_ampersand(set1, set2))
