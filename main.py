"""
* Author: Cesar M. Gonzalez R.
* Company: Teams International
* CreateAt: 07/12/2022

Data Capture project

"""
import csv
import os.path
import sys
import time


from data_capture import DataCapture

argv = sys.argv[1:]

# Check if csv file exist
if not os.path.exists(argv[0]):
    print("script cannot access to {}".format(argv[0]))
    exit()

# Populate data capture object
capture = DataCapture()
stat = None
# Read CSV file
with open(argv[0], newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            number = int(str(row[0]).strip())
            if 0 > number > 100:
                raise ValueError("number is not positive or is greater than 1000")
            start = time.time_ns()
            capture.add(number)
            end = time.time_ns()
            print('time ns: ', end - start)
        except ValueError as verr:
            print("The value: '{0}' is not a number or is negative or is greater than 1000".format(row))
            exit()

# build the stat
start = time.time_ns()
stat = capture.build_stats()
end = time.time_ns()
print('time ns: ', end - start)


print("""
Welcome to DataCapture used to apply basic statistics (les, greater, between) to a list of positive numbers (0,1000)
with a time complexity O(1) for add, les, greater, between operations
""")
print("""
How use it: enter the operations followed by the a positive number(s), The operation accepted are [less, greater, between]
examples:
    - less 5
    - greater 10
    - between 2,30 
To close the program enter exit
""")

while True:
    # Enter operation command
    op = input("""Enter the operation and number(s):""")
    if op.strip().lower() == 'exit':
        exit()
    args = op.split(' ')
    if len(args) != 2:
        print("enter all the arguments please")
        continue
    operation, number_s = args[0], args[1]
    match operation:
        case 'less':
            number = int(str(number_s).strip())
            # Apply input validations, the number must be positive
            if number < 0:
                print("The number is negative: {0}".format(number))
            start = time.time_ns()
            list_result = stat.less(number)
            end = time.time_ns()
            print('time ns: ', end - start)
        case 'greater':
            number = int(str(number_s).strip())
            # Apply input validations, the number must be positive
            if number < 0:
                print("The number is negative: {0}".format(number))
            start = time.time_ns()
            list_result = stat.greater(number)
            end = time.time_ns()
            print('time ns: ', end - start)
        case 'between':
            start_number, end_number = str(number_s).strip().split(',')
            start_number, end_number = int(start_number), int(end_number)
            # Apply input validations, both numbers must be positive
            if start_number < 0:
                print("The start number is negative: {0}".format(start_number))
            if end_number < 0:
                print("The end number is negative: {0}".format(end_number))
            if start_number > end_number:
                print("Start number: {0} is greater than the end number: {1}".format(start_number, end_number))
            start = time.time_ns()
            list_result = stat.between(start_number, end_number)
            end = time.time_ns()
            print('time ns: ', end - start)
        case _:
            print(" Select a valid operation [less, greater, between]")
            list_result = None

    print(list_result)
