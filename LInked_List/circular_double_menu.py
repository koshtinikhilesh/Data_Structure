"""
circular_list_menu.py

Date: 28 May 2019

Author: Koshti Nikhilesh


Goal:- Develop a circular linked list with menu items to add , delet and get the data.

Options:-
 1 Insert
 2 Remove
 3 Display the list
 4 quit
Enter your choice:-
"""

# circular double linked list with menu option
from time import sleep
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class CreateList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def insert_end(self, data):
        print('Insert end:- ', data)
        node = Node(data)
        # check for the first element
        if self.head.data is None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head

    def insert_begin(self, data):
        print('Insert begin:- ', data)
        node = Node(data)
        # check for the first element
        if self.head.data is None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = node

    def insert_after(self, data, element):
        print('Insert {} after {}'.format(data, element))
        node = Node(data)

        # entering after certain node data
        current = self.head

        while current.data != element:
            print("Ierating over element:- {}".format(current.data))
            current = current.next
            sleep(1)
        node.next = current.next
        current.next = node

    def removal_end(self):
        print('Removal end:- ')

        # check the list if it is less than 1
        link_list = self.display()
        length = len(link_list)

        # check for the first element
        if length <= 1:
            return "Cannot delete the items in list"

        else:
            current = self.head
            while current.next is not self.tail:
                print("iterating:- {}".format(current.next))
                current = current.next
            current.next = self.head


    def removal_begin(self):
        print('Removal begin')

        # check the list if it is less than 1
        link_list = self.display()
        length = len(link_list)

        print("list is {} and length is:- {}".format(link_list, length))

        # check for the first element
        if length <= 1:
            return "Cannot delete the items in list"
        else:

            # delete from begin
            self.tail.next = self.head.next
            self.head = self.head.next
            return "removed successfully"


    def removal_after(self, element):
        print('Removal after {}'.format(element))
        # check the list if it is less than 1
        link_list = self.display()
        length = len(link_list)
        if length <= 1:
            return "Cannot delete the items in list"
        else:
            current = self.head
            while current.next.data is not element:
                print("iterating:- {}".format(current.next.data))
                current = current.next
                sleep(1)

            # delete the element
            current.next = current.next.next
            return " removed successfully"

    def display(self):
        print('Display the list')
        elements = []
        current = self.head

        if self.head.data is None:
            print("list is empty")

        else:
            while current.next != self.head:
                print(current.data)
                elements.append(current.data)
                current = current.next

            print(current.data)
            elements.append(current.data)
        return elements


def main_loop(loop):
    print("Options:-  \n 1 Insert \n 2 Remove\n 3 Display the list\n 4 quit")
    while loop:
        try:
            choice = int(raw_input("Enter your choice:-   "))
            if choice not in range(1, 5):
                print("Please enter between 1 to 5")
            else:
                loop = False
        except:
            print("Received invalid value")

    dict_list = {'1': 'insert', '2': 'remove', '3': 'display', '4': 'quit'}
    print("\n You have selected:- ", choice)
    return choice


if __name__ == '__main__':
    loop = True
    cl = CreateList()
    print('-' * 50 + " Circular Doubly Linked List" + '-' * 50)

    choice = main_loop(loop)

    while choice != 'quit':
        if choice == 1:
            print('-' * 50 + " Insertion of Linked List" + '-' * 50)
            print("Options:-  \n 1 Insert at beginning \n 2 Insertion at end \n 3 Insert after some node")
    
            # expected input for insertion in linked list
            insert_loop = True
            while insert_loop:
                try:
                    insert_choice = int(raw_input("For insertion, Enter your choice:-   "))
                    if insert_choice not in range(1, 4):
                        print("Please enter between 1 to 3")
                    else:
                        insert_loop = False
                except:
                    print("Received invalid value")
            print('\n You have selected:- ', insert_choice)

            # enter your data
            insert_data = raw_input("Enter your data:- ")
            insert_methods = {1: 'insert_begin', 2: 'insert_end', 3: 'insert_after'}

            # execute the respective methods
            print("Choice:- ", insert_choice)
            method_name = insert_methods.get(insert_choice)
            # check for insert after
            if int(insert_choice) == 3:
                extra_data = raw_input("Enter your node data:- ")
                data = cl.display()
                print("Data present in linked list is {}".format(data))
                # check for empty list:
                if data:
                    if extra_data not in data:
                        print("respective data is not present:- Inserting at the end")
                        cl.insert_end(insert_data)
                    else:
                        cl.insert_after(insert_data, extra_data)
                else:
                    cl.insert_after(insert_data, extra_data)
            else:
                print('methods name is :-', (method_name))
                getattr(cl, method_name)(insert_data)
            print(cl.display())
            choice = main_loop(loop)

        # Removal methods
        elif choice == 2:
            print('-' * 50 + " Removal of Linked List" + '-' * 50)
            print("Options:-  \n 1 Removal at beginning  \n 2 Removal at end \n 3 Removal after some node")
    
            # expected input for removal in linked list
            removal_loop = True
            while removal_loop:
                try:
                    removal_choice = int(raw_input("For removal, Enter your choice:-   "))
                    if removal_choice not in range(1, 4):
                        print("Please enter between 1 to 3")
                    else:
                        removal_loop = False
                except:
                    print("Received invalid value")
            print('\n You have selected:- ', removal_choice)

            # enter your data
            # removal_data = raw_input("Enter your data:- ")
            removal_methods = {1: 'removal_begin', 2: 'removal_end', 3: 'removal_after'}

            # execute the respective methods
            print("Choice:- ", removal_choice)
            method_name = removal_methods.get(removal_choice)

            # check for insert after
            if int(removal_choice) == 3:
                extra_data = raw_input("Enter your node data:- ")
                data = cl.display()
                print("Data present in linked list is {}".format(data))
                # check for empty list:
                if data:
                    if extra_data not in data:
                        print("respective data is not present: Not removing items")
                    else:
                        cl.removal_after(extra_data)
                else:
                    cl.removal_after(extra_data)
            else:
                print('methods name is :-', (method_name))
                print("Result of removal method:- ", getattr(cl, method_name)())

            print(cl.display())
            choice = main_loop(loop)

        # display the linked list
        elif choice == 3:
            print('-' * 50 + " Display the Linked List" + '-' * 50)
            elements = cl.display()
            print("Linked list is {} and length is {}".format(elements, len(elements)))
            choice = main_loop(loop)

        elif choice == 4:
            print('-' * 50 + "  quit " + '-' * 50)
            print('Linked list is {}'. format(cl.display()))
            sys.exit()
