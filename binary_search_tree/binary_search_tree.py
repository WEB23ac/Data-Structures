from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # * current variable begins as root and becomes children as evaluation proceeds
        current = self
        # * Base Cases -- if there are no children in direction, insert new BinarySearchTree w/ given value

# * If self.value is less than value, check the left child
        if self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)
        if self.value <= value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # print(f'evaluating :: self.value = {self.value} || target = {target}')
        if self.value == target:
            return True
        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)
        if self.value < target:
            if self.right is not None:
                return self.right.contains(target)
        else:
            return False

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
