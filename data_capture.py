"""
* Author: Cesar M. Gonzalez R.
* Company: Teams International
* CreateAt: 07/11/2022

Data Capture, accepts numbers (collection of integers), returns statistics operations based on them

"""
from stats import Stats


class Node:
    """
    Nodes object to build a linked list and keep the O(1) adding elements
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class DataCapture:
    """
    Capture the input numbers
    """
    __head_node: Node = None  # Node head in linked list
    __tail_node: Node = None  # Node tail in linked list

    def add(self, number: int):
        """
        Overwrite add set method. Add an element to a set.

        This has effect if the element is already present. add an element to a set
        """
        # Apply input number validations
        if not isinstance(number, int):
            raise ValueError("The input value: '{0}' is not a number".format(number))
        if not number > 0:
            raise ValueError("The number: '{0}' is not a positive number".format(number))

        # Add new item to linked list
        if self.__head_node:
            self.__tail_node.next = Node(number)
            self.__tail_node = self.__tail_node.next
        else:
            self.__tail_node = self.__head_node = Node(number)
        print("Number '{0}' was added in DataCapture".format(number))

    def build_stats(self):
        """
        Close the list of numbers added, no more numbers can be added after this action
        """

        print("Build starts...")
        # init adjacency matrix dictionary
        adjacency_matrix_dict = {}
        # Sort numbers by ascending
        self.__sort()

        # Create Adjacency Matrix using consecutive nodes tuples in dictionary
        current_node: Node = self.__head_node
        next_node: Node = self.__head_node

        # create the tuple (x,y) to map the values between 0 and 1000
        for x_axis in range(0, 1001):
            # This list contains the final result
            list_numbers = []
            for y_axis in range(0, 1001):
                # Based on the algorithm is not needed map the values when x > y, because for less operation is used
                # (0,y) pair
                if x_axis > y_axis:
                    continue

                # Loop through all the repeated values
                while x_axis > current_node.data:
                    next_node = current_node = current_node.next
                    if x_axis > self.__tail_node.data:
                        current_node = self.__tail_node
                        break

                # Loop through all the y values to get the pair (x,y) mapped
                if x_axis <= current_node.data and y_axis == next_node.data:
                    while y_axis == next_node.data:
                        list_numbers.append(next_node.data)
                        next_node = next_node.next
                        if next_node is None:
                            next_node = current_node
                        if next_node.data == self.__tail_node.data:
                            break

                # Add a new item into dict using (x,y) pair and the result is the list of values into this range
                adjacency_matrix_dict[(x_axis, y_axis)] = list_numbers.copy()

        print("Data built successfully")
        # Return Statistics object
        return Stats(adjacency_matrix_dict, self.__tail_node.data, self.__head_node.data)

    def __quicksort(self, head, tail):
        """
        Apply quick sort algorithm to order a linked list by ascending order, the algorithm used is based on the next
        post: https://stackoverflow.com/a/58767472/8501305
        :param head: First item in linked list
        :param tail: Last item in linked list
        :return: Return release Node and target Node
        """
        if head is tail:
            return head, tail
        tlt = hlt = Node(None)  # head, tail < pivot list
        teq = heq = Node(None)  # head, tail = pivot list
        tgt = hgt = Node(None)  # head, tail > pivot list
        curr = pivot = head
        end = tail.next
        while curr is not end:
            if curr.data < pivot.data:
                tlt.next = curr
                tlt = curr
            elif curr.data == pivot.data:
                teq.next = curr
                teq = curr
            else:
                tgt.next = curr
                tgt = curr
            curr = curr.next
        heq = heq.next  # at least 1 node (should release node)
        if hlt is tlt:  # if none < pivot
            hlt = heq  # (should release dummy node)
        else:  # else recurse on list < pivot
            hlt = hlt.next  # (should release dummy node)
            hlt, tlt = self.__quicksort(hlt, tlt)
            tlt.next = heq
        if hgt is tgt:  # if none > pivot
            tgt = teq
        else:  # else recurse on list > pivot
            hgt = hgt.next  # (should release dummy node)
            hgt, tgt = self.__quicksort(hgt, tgt)
            teq.next = hgt
        return hlt, tgt

    def __sort(self):
        """
        Sort linked list using quick sort algorithm, the time complexity for this algorithm if O(log(n))
        https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/
        :return: None
        """
        print("Sort data...")
        # if empty list return
        if self.__head_node is None:
            return
        # sort the linked list
        self.__head_node, self.__tail_node = self.__quicksort(self.__head_node, self.__tail_node)
        self.__tail_node.next = None
        return
