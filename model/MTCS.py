from utils import exception

class Node:
    """This class defines the nodes of a tree"""
    def __init__(self, parent, state):
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
        self.visit_count = 0
        self.reward = 0
        self.children = []