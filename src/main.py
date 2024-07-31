import random
from typing import List
from typing import Tuple

class Func:
    def __init__(self, func: function, prob: int, args:int):
        self.func = func
        self.args = args
        self.prob = prob
        
class Node:
    def __init__(self, func: function, children: List['Node']):
        self.func = func
        self.children = children

def create_tree(func_list: List[Func], max_depth) -> Node:
    if max_depth == 1:
        avail_funcs = filter(lambda func: func.args == 2, func_list)
        rand_num = random.randint(0, sum(map(lambda func: func.prob, avail_funcs))-1)
        accumulator = 0
        for func in avail_funcs:
            accumulator += func.prob
            if rand_num < accumulator:
                rand_func = func
            return Node(rand_func.func, [])
    else:
        rand_num = random.randint(0, sum(map(lambda func: func.prob, func_list))-1)
        accumulator = 0
        for func in func_list:
            accumulator += func.prob
            if rand_num < accumulator:
                rand_func = func
                return Node(rand_func.func, [create_tree(func_list,max_depth-1)])

def eval_tree_at_pixel(node: Node, coords: Tuple, ascii_map):
    

def eval_tree_over_grid(tree, size, ascii_map):
    return

def main(func_list, size, ascii_map, max_depth):
    return

if __name__ == "__main__":
    main()