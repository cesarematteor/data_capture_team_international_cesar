"""
* Author: Cesar M. Gonzalez R.
* Company: Teams International
* CreateAt: 07/11/2022

Statistics, execute statistics operations: less, greater, between

"""


class Stats:

    def __init__(self, adjacency_matrix_dict: {}, max_value: int, min_value: int):
        self.__adjacency_matrix_dict = adjacency_matrix_dict
        self.max_value = max_value
        self.min_value = min_value

    def less(self, number: int) -> [int]:
        """
        Defines a list of numbers less than the given input number
        :param number: number to compare
        :return: list of integer numbers
        """
        # Return list of values mapped into key (min_value_in_list, number - 1), this keep O(1)
        return self.__adjacency_matrix_dict[(self.min_value, number - 1)]

    def between(self, start_number: int, end_number: int) -> [int]:
        """
        Defines a list of numbers between the given input start-number and end-number
        :param start_number: start number to compare
        :param end_number: end number to compare
        :return: list of integer numbers
        """
        # Return list of values mapped into key (start_number, end_number), this keep O(1)
        return self.__adjacency_matrix_dict[(start_number, end_number)]

    def greater(self, number: int) -> [int]:
        """
        Defines a list of numbers greater than the given input number
        :param number: number to compare
        :return: list of integer numbers
        """
        # Return list of values mapped into key (number + 1, max_value_in_list), this keep O(1)
        return self.__adjacency_matrix_dict[(number + 1, self.max_value)]

