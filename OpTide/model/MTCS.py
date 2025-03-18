from OpTide.utils import peptide
from OpTide.utils import get_score

class Node:
    """This class defines the nodes of a tree"""
    def __init__(self, parent=None, state=None, mutate_strategy=peptide.random_mutation):
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

        if state is None:
            if parent is None:
                self.state = peptide.gen_random_peptide()
            else:
                self.state = mutate_strategy(parent.state)
        else:
            self.state = state

        self.visit_count = 0
        self.reward = 0
        self.children = []

    def add_child(self):
        """Add a child to the node"""
        child = Node(parent=self)
        self.children.append(child)
        self.reward += (get_score(child.state)-get_score(self.state))
        return child


class Tree:
    """This class defines the tree for the Monte Carlo Tree Search"""
    def __init__(self, nodes=None):
        if nodes is None:
            self.head = Node
            self.nodes = []

if __name__ == "__main__":
    pass