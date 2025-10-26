set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


def using_for_loop(set1, set2):
    new_set = set()
    for item in set1:
        if item not in set2:
            new_set.add(item)

    for item in set2:
        if item not in set1:
            new_set.add(item)
    return new_set


def using_symm_diff_func(set1, set2):
    new_set = set1.symmetric_difference(set2)
    return new_set


def using_caret_sign(set1, set2):
    new_set = set1 ^ set2
    return new_set


print(using_caret_sign(set1, set2))
