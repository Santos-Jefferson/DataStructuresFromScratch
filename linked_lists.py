class Node:
    """
    Class to model a node for a linked list
    """

    def __init__(self, item):
        """
        Method to initialize a node with item value and next as None
        :param item:
        """
        self.item = item
        self.next = None


class LinkedList:
    """
    Class do model a single Linked List
    """

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Insert a node at the beginning of a LL
        :param data: the value to be added
        """
        new_node = Node(data)  # New node created
        new_node.next = self.head  # the next in new node will receive the first node(head) from current LL
        self.head = new_node  # the first node will receive the new node

    def insert_after(self, node, data):
        pass

    def insert_at_end(self, data):  # Or like .append()
        new_node = Node(data)  # new node created

        if self.head is Node:  # if the LL is empty
            self.head = new_node  # new node is inserted in the LL
            return  # and return (exit the function)

        current = self.head  # current will be the first node of LL
        while current.next:  # while there is a next value
            current = current.next  # continue going to the next node

        current.next = new_node  # When while get FALSE, set to new node

    def delete_node(self, position):  #
        pass

    def delete_first_ocurrence(self, data):  #
        pass
