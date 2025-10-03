nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]


def flatten_list(nested_list: list) -> list:
    flat_list = []
    for row in nested_list:
        if type(row) is list:
            for i in row:
                flat_list.append(i)
        else:
            flat_list.append(row)
    return flat_list


# alternative
def flat_list(nested_list):
    flat_list = []
    for row in nested_list:
        if isinstance(row, list):
            for i in row:
                flat_list.append(i)
        else:
            flat_list.append(row)
    return flat_list


flatted_list = flat_list(nested_list)
print(f"Flatted list: {flatted_list}")
