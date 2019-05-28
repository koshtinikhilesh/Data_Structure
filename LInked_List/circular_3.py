"""
circular_list.py

Date: 28 May 2019

Author: Koshti Nikhilesh


Goal:- Develop a circular linked list with get, delete and insert node in python

add node
get the size of list

"""

# class with node object
class Node(object):

    def __init__(self, data):
        """
        :param data:- Data to be inserted into list
        """
        self.data = data
        self.next = None

    def get_next(self):
        """
        get the next element of the list
        """
        return self.next_node

    def set_next(self, val):
        """
        set the node into the list
        """
        self.nex_node = val

    def get_data(self):
        """
        get the data value from the list
        """
        return self.data

    def set_data(self, value):
        self.data = value


# class for circular linked list
class circularLinkedList(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size

    # Add value to linked list at location
    def addNode(self, data):
        newNode = Node(data)
        temp = self.root

        # make the list as circular by connceting head to the last node
        newNode.next = self.root

        # check for the root value( if data is present in the list)
        if self.root is not None:
            while(temp.next != self.root):
                temp = temp.next
            temp.next = newNode
        else:
            # if data is not present in the list
            newNode.next = newNode

            # assign the new value to the root value
            self.root = newNode

        print('Root value is ', self.root.data)
        self.size += 1


if __name__ == '__main__':
    print("Create the instance of Circular Linked list")
    myList = circularLinkedList()

    print("Adding 4 to the list")
    myList.addNode(4)

    print("Adding 6 into the list")
    myList.addNode(6)

    print("Total number of element:- ")
    print(myList.get_size())
