from copy import deepcopy

def dict_from_task(task):
    final_dct = {}
    dct = deepcopy(vars(task))

    for k, v in dct.items():
        final_dct[k[1:]] = v

    del final_dct['diagram']
    
    return final_dct