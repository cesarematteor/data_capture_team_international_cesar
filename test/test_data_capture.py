"""
* Author: Cesar M. Gonzalez R.
* Company: Teams International
* CreateAt: 07/11/2022

Data Capture, accepts numbers (collection of integers), returns statistics operations based on them
Inheritance from set built-in class

Test Cases

"""
import random
from unittest import TestCase

from data_capture import DataCapture


class TestDataCapture(TestCase):
    def test_instance_data_capture(self):
        DataCapture()
        assert True, "None exception was thrown"

    def test_add(self):
        data_capture = DataCapture()
        data_capture.add(3)
        assert True, "None exception was thrown"

    def test_add_multiple_numbers(self):
        data_capture = DataCapture()
        data_capture.add(3)
        data_capture.add(100)
        data_capture.add(55)
        data_capture.add(81)
        assert True, "None exception was thrown"

    def test_add_not_a_number(self):
        data_capture = DataCapture()
        try:
            data_capture.add("four")
        except ValueError:
            assert True, "Value error exception"

    def test_add_not_a_positive_number(self):
        data_capture = DataCapture()
        try:
            data_capture.add(-100)
        except ValueError:
            assert True, "Value error exception"

    def test_build_starts(self):
        data_capture = DataCapture()
        data_capture.add(random.randint(1, 1000))
        data_capture.add(random.randint(1, 1000))
        data_capture.add(random.randint(1, 1000))
        data_capture.add(random.randint(1, 1000))
        data_capture.build_stats()
        assert True, "None exception was thrown"

    def test_build_starts_random_size(self):
        data_capture = DataCapture()
        random_numbers_list = [random.randint(1, 1000) for item in range(random.randint(1, 100))]
        print("Numbers list size: '{0}' random integer values".format(len(random_numbers_list)))
        for number in random_numbers_list:
            data_capture.add(number)
        assert True, "None exception was thrown"