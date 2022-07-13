## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How use it](#how-use-it)

## General info
Data Capture program for TEAM INTERNATIONAL demo.
	
## Technologies
Project is created with:
* Python: 3.10
	
## Setup
To run this project, execute main.py and as argument include your csv path file:
```
python main.py "{positive_list_numbers_csv_file_path.csv}"
```
There is a csv example in data folder, you can use it as reference.

## How use it
Follow the instructions:
Enter the operations followed by a positive number(s), The operation accepted are [less, greater, between]

examples:
* less 5
* greater 10
* between 2,30

To close the program enter exit

## How it works
The program going to read the csv file to populate the capture object using a custom linked list
to keep O(1) adding new items.

Once the list is populated, the next action is sort the list and generate an Adjacency Matrix to keep the 
less, greater, and between operations on O(1)  


