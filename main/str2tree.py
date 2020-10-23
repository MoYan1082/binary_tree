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
            return TreeNode(val = token, left = self.subtree(), right = self.subtree())
        else :
            self.error()

    def get_root(self):
        token = self.get_next_token()
        if token.isnumeric():
            return TreeNode(val = token, left = self.subtree(), right = self.subtree())

        else :
            self.error()


def string2Tree(string):
    lst = string.split()
    parser = Parser(lst)

    return parser.get_root()

if __name__ == "__main__":
    s = "1 2 4 null null 5 null null 3 6 null null null"
    root = string2Tree(s)

    visualization.draw(root, 4)
