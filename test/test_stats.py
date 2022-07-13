"""
* Author: Cesar M. Gonzalez R.
* Company: Teams International
* CreateAt: 07/11/2022

Statistics, execute statistics operations: less, greater, between
Inheritance from set built-in class

Test Cases

"""
import random
from unittest import TestCase

from data_capture import DataCapture


class TestDataCaptureOperations(TestCase):

    def test_less(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        stats = data_capture.build_stats()
        less_list = stats.less(4)
        print(less_list)
        assert less_list == [3, 3], "None exception was thrown"

    def test_less_long_set(self):
        data_capture = DataCapture()
        random_numbers_list = [random.randint(1, 1000) for item in range(random.randint(100, 1000))]
        print("Numbers list size: '{0}' random integer values".format(len(random_numbers_list)))
        for number in random_numbers_list:
            data_capture.add(number)
        less_number = random_numbers_list[int(len(random_numbers_list) / 2)]
        print("numbers less than: ", less_number)
        stats = data_capture.build_stats()
        less_list = stats.less(less_number)
        print(less_list)
        assert True, "None exception was thrown"

    def test_less_negative_number(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        stats = data_capture.build_stats()
        less_list = stats.less(-10)
        print(less_list)
        assert less_list == [3, 3], "None exception was thrown"

    def test_between(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        stats = data_capture.build_stats()
        between_list = stats.between(3, 6)
        print(between_list)
        assert between_list == [3, 3, 4, 6], "None exception was thrown"

    def test_between_long_set(self):
        data_capture = DataCapture()
        random_numbers_list = [random.randint(1, 1000) for item in range(random.randint(100, 1000))]
        print("Numbers list size: '{0}' random integer values".format(len(random_numbers_list)))
        for number in random_numbers_list:
            data_capture.add(number)
        start_number = random_numbers_list[int(len(random_numbers_list) / 4)]
        end_number = random_numbers_list[int(len(random_numbers_list) / 2)]
        print("numbers between {0} and {1} ".format(start_number, end_number))
        stats = data_capture.build_stats()
        between_list = stats.between(start_number, end_number)
        print(between_list)
        assert True, "None exception was thrown"

    def test_between_any_negative_number(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        stats = data_capture.build_stats()
        between_list = stats.between(-3, 6)
        print(between_list)
        assert between_list == [3, 3, 4, 6], "None exception was thrown"

    def test_between_both_negative_numbers(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        stats = data_capture.build_stats()
        between_list = stats.between(-3, -6)
        print(between_list)
        assert between_list == [3, 3, 4, 6], "None exception was thrown"

    def test_between_start_number_greater_than_end_number(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        stats = data_capture.build_stats()
        between_list = stats.between(6, 3)
        print(between_list)
        assert between_list == [3, 3, 4, 6], "None exception was thrown"

    def test_greater(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        stats = data_capture.build_stats()
        greater_list = stats.greater(4)
        print(greater_list)
        assert True, "None exception was thrown"

    def test_greater_long_set(self):
        data_capture = DataCapture()
        random_numbers_list = [random.randint(1, 1000) for item in range(random.randint(100, 1000))]
        print("Numbers list size: '{0}' random integer values".format(len(random_numbers_list)))
        for number in random_numbers_list:
            data_capture.add(number)
        greater_number = random_numbers_list[int(len(random_numbers_list) / 2)]
        print("numbers greater than: ", greater_number)
        stats = data_capture.build_stats()
        greater_list = stats.greater(greater_number)
        print(greater_list)
        assert True, "None exception was thrown"

    def test_greater__negative_number(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(9)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(6)
        stats = data_capture.build_stats()
        greater_list = stats.greater(-4)
        print(greater_list)
        assert True, "None exception was thrown"
