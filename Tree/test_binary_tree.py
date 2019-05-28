"""
Date:- 28 May 2019
Author:- Koshti Nikhilesh

Develop a Binary search tree with ascending values

"""
class Node(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:

            if data < self.data:

                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

                if self.right is None:
                    self.rightr = Node(data)
                else:
                    self.right.insert(data)                    


        else:
            self.data = data

    def print_tree(self):
    	if self.left:
    		self.left.print_tree()
    	print(self.data)
    	if self.right:
    		self.right.print_tree()

root = Node(12)
root.insert(11)
root.insert(10)


root.print_tree()
