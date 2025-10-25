dict1 = {"a": 1, "b": 2, "c": 3}  # All values unique
dict2 = {"x": 10, "y": 20, "z": 10}  # Value 10 is duplicated
dict3 = {}  # Empty dictionary (all values are vacuously unique)


def check_duplicate(items: dict):
    new_set = set(items.values())
    if len(items.values()) != len(new_set):
        return False
    return True


print(check_duplicate(dict3))
