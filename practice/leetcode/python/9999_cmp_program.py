def cmp_dict(d1, d2):
    for key in d1:
        if key in d2:
            v1 = d1[key]
            v2 = d2[key]
            if not cmp_vars(v1, v2):
                print(f"key mismatch: '{key}':\n{v2}, {v2}")
                return False
        else:
            print(f"key '{key}' is not present in second dictionary")
            return False

    for key in d2:
        if not key in d1:
            print(f"key '{key}' is present extra in second dictionary")
            return False

    return True

def cmp_list(l1, l2):
    if len(l1) != len(l2):
        print(f"List length mismatch: {len(l1)} vs {len(l2)}")
        return False

    for i in range(len(l1)):
        if not cmp_vars(l1[i], l2[i]):
            print(f"List element at Index {i} mismatch: {l1[i]} vs {l2[i]}")
            return False

    return True

def cmp_vars(v1, v2) -> bool:
    if type(v1) != type(v2):
        print(f"Type mismatch: {type(v1)} vs {type(v2)}")
        return False

    if isinstance(v1, dict):
        return cmp_dict(v1, v2)

    if isinstance(v1, (list, tuple)):
        return cmp_list(v1, v2)

    if v1 != v2:
        print(f"Value mismatch: {v1} vs {v2}")
        return False

    return True
