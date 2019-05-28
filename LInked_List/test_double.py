"""
Date:- 28 May 2019
Author:- Koshti Nikhilesh

Develop a Double linked list with both the sides of pointer as per definition

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def traverse(self):
    	node = self
    	while node is not None:
    		print(node.val)
    		node = node.next





if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)


    # next value
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9

    # previous value
    node2.previous = node1
    node3.previous = node1
    node4.previous = node1
    node5.previous = node1
    node6.previous = node1
    node7.previous = node1
    node8.previous = node1
    node9.previous = node1

    print(node1.traverse())