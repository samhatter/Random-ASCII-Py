# tree: {"func":func, "children":[...]}
# size: {"height":height, "width":width}
# ascii_map: [{"threshold":thresh0, "character":char0}, {"threshold":thresh1, "character":char1}]
# func_dict: {"1":[{"prob":prob0, "func":func0}]}
# coords: {"x":x, "y":y}

import random

def create_tree(func_dict, max_depth):
    if max_depth == 1:
        avail_funcs = func_dict["2"]
        rand = random.uniform(0, sum([func["prob"] for func in avail_funcs]))
        func = max(avail_funcs, key=lambda func: func["prob"] if func["prob"] < )
        return {}
    else:
        rand = random.uniform(0, 1)
        return create_tree(func_dict_max_depth-1)

def eval_tree_at_pixel(tree, coords, ascii_map):
    return

def eval_tree_over_grid(tree, size, ascii_map):
    return

def main(func_dict, size, ascii_map, max_depth):
    return

if __name__ == "__main__":
    main()