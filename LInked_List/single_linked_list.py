"""
Date:- 28 May 2019
Author:- Nikhilesh Koshti

Develop a single linked list with print and add methods

"""

class Node(object):
    def __init__(self, data):
        self.data  = data
        self.next = None


class Single_List(object):
    def __init__(self):
        self.head = None
        # self.temp = self.head

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def print_list(self):
        current = self.head
        while current.next is not None:
            print(current.data)
            current = current.next

        print(current.data)



list1 = Single_List()
list1.insert('1')
list1.insert('2')
list1.insert('3')
list1.insert('4')
list1.insert('5')
list1.insert('6')
list1.insert('17')
list1.print_list()
