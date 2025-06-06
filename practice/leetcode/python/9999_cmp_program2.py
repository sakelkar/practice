def cmp_list(l1, l2) -> bool:
    if len(l1) != len(l2):
        print(f"Length mismatch in list: {len(l1)} vs {len(l2)}")
        return False

    for i in range(len(l1)):
        v1 = l1[i]
        v2 = l2[i]
        if not cmp_vars(v1, v2):
            print(f"List value mismatch at index '{i}':\n{v1}\n{v2}")
            return False

    return True

def cmp_dict(d1, d2) -> bool:
    #For every key in d1, it must be found in d2
    for key in d1:
        if key in d2:
            v1 = d1[key]
            v2 = d2[key]
            if not cmp_vars(v1, v2):
                print(f"key mismatch: '{key}:\n{v1}\n{v2}'")
                return False
        else:
            print(f"key '{key}' is not found in second dictionary")
            return False

    for key in d2:
        if not key in d1:
            print(f"key '{key}' is not found in first dictionary")
            return False

    return True

def cmp_vars(v1, v2) -> bool:
    #First check type to be same
    if type(v1) != type(v2):
        print(f"Type mismatch: {type(v1)} vs {type(v2)}")
        return False

    #Check if dictionary
    if isinstance(v1, dict):
        return cmp_dict(v1, v2)

    #Check if list or tuple
    if isinstance(v1, (list, tuple)):
        return cmp_list(v1, v2)

    #Check value if simple variable
    if v1 != v2:
        print(f"value mismatch: {v1} vs {v2}")
        return False

    return True
