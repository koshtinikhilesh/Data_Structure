'''
Date:- 28 May 2019
Author:- Koshti Nikhilesh

Add two linked lists from right to left
e.g. 1->2->3 + 8->7 => 123+87 = 210

depend on the one of the best github repo for data structure owner.
'''

class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None

    def traverse(self):
        # traverse the value
        print("traversing the value")
        node = self
        while node is not None:
            print("VALUES:- ", node.val)
            node = node.next
    def length(self):
        length = 0
        node = self
        while node != None:
            node = node.next
            length += 1
        return length


def sum_linked_list(p1, p2):
    print('adding the sum of linked list')
    sum1 = 0
    length = p1.length() - 1

    while p1.next is not None:
        print p1.val
        print p1.val
        sum1 = sum1 + p1.val * (10 ** length)
        print sum1
        p1 = p1.next
        length = length - 1
    print "sum is :- ", sum1 + p1.val * (10 ** length)
    sum2 = 0
    length2 = p2.length() - 1

    while p2.next is not None:
        print p2.val
        print p2.val
        sum2 = sum2 + p2.val * (10 ** length2)
        print sum2
        p2 = p2.next
        length2 = length2 - 1
    print "sum2 is :- ", sum2 + p2.val * (10 ** length2)
 
    print("Total sum:- ", sum1 + sum2)

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(9)
    node5 = Node(8)
    node6 = Node(7)
    node1.next = node2
    node2.next = node3
    node4.next = node5
    node5.next = node6
    # sum1 = sum_linked_lists_forward(node1,node4) # 123 + 987 = 1110
    # sum2 = sum_linked_lists_forward(node1,node5) # 123 + 87 = 210
    node1.traverse()
    node4.traverse()
    print(node1.length())
    # sum2.traverse()
    print(sum_linked_list(node1, node4))