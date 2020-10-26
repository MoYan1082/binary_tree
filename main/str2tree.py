#!/usr/bin/python3

import visualization

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

'''
Operations
'''

class Parser(object):
    def __init__(self, lst):
        self.lst = lst
        self.cur_pos = 0
        self.depth = 0
        self.cur_depth = 0

    def get_next_token(self):
        if self.cur_pos < len(self.lst):
            tmp = self.cur_pos
            self.cur_pos += 1
            return self.lst[tmp]

        else:
            return None

    def error(self):
        raise Exception("Invalid Syntax!")


    def subtree(self):

        token = self.get_next_token()
        if token == "null":
            return None
        elif token == None:
            return None
        elif token.isnumeric:
            self.cur_depth += 1

            if self.cur_depth > self.depth:
                self.depth = self.cur_depth

            node = TreeNode(val = token, left = self.subtree(), right = self.subtree())
            self.cur_depth -= 1

            return node
        else :
            self.error()


    def get_root(self):
        token = self.get_next_token()
        if token.isnumeric:
            self.depth += 1
            self.cur_depth += 1
            return TreeNode(val = token, left = self.subtree(), right = self.subtree())

        else :
            self.error()

    def get_depth(self):
        return self.depth


def string2Tree(string):
    lst = string.split()
    parser = Parser(lst)
    
    root = parser.get_root()
    depth = parser.get_depth()

    return root, depth

if __name__ == "__main__":
    s = "1 2 4 null null 5 null null 3 6 7 null null null null"
    # s = input()
    root, depth = string2Tree(s)


    visualization.draw(root, depth)
