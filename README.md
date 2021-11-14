# ioet-exercise

## Problem

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours.

## How to run the program locally?

### Download

First of all, clone the repository:

(Before download, __[Python3](https://www.python.org/downloads/)__ is required)

```
git clone https://github.com/epulla/ioet-exercise.git
```

### Usage

Then, go to the project folder and run the following command:

For Windows:

```
> py .\src\main.py <input-file>
```

For Linux/Mac:

```
$ python3 ./src/main.py <input-file>
```

You can use [data.txt](https://github.com/epulla/ioet-exercise/blob/main/data.txt) as default for your __<input-file>__ or you can create a new txt file with new data

## How to test it locally?

[test.py](https://github.com/epulla/ioet-exercise/blob/main/test.py) is the default testing file and you can run it with the following command:

For Windows:

```
> py test.py
```

For Linux/Mac:

```
$ python3 test.py
```

This file uses [unittest](https://docs.python.org/3/library/unittest.html) built-in library of python3. You can change it if you want :)

## Solution

### Why python3?

Python3 was chosen because of string slicing (easy string manipulation), built-in unit testing library, easy file reading and a object oriented approach.

### Overview

The problem was solved using classes, built-in python dictionaries (data structure similar to a Hash Map), Boolean Algebra and elements combination algorithm. Most of methods, algorithms and structures of the program are located in __[src/util.py](https://github.com/epulla/ioet-exercise/blob/main/src/util.py)__, and the logic of the main function is in __[src/main.py](https://github.com/epulla/ioet-exercise/blob/main/src/main.py)__.

The main idea of the solution was to apply `Divide and Conquer` approach, so the problem was divided in the following subproblems: 
- Checking if hour ranges are overlapped.
- Associating hour ranges to days as a schedule of someone.
- Comparing schedules.
- Combining people's schedules to have unique pairs of them to avoid comparing the same element or inverted pairs.

The solution begins by creating a class named __HourRange__ that handles hour ranges easily. The attributes of the class had to be a start hour and end hour in the most simple way. Next, a method was needed to allow us to compare ranges between two instance of this class. This comparison checks if the hour ranges between instances are overlapping, and that can be considered as a coincidence in schedule. This was solved using Boolean Algebra: 

> There is HourRangeA and HourRangeB (each of them has its startTime and endTime). There is no overlapping between both hour ranges if neither startTimeA > endTimeB nor endTimeA < startTimeB. The expression is: `not(startTimeA > endTimeB or endTimeA < startTimeB)`, which can be translated to `not(startTimeA > endTimeB) and not(endTimeA < startTimeB)` or, more specifically, `startTimeA <= endTimeB and endTimeA >= startTimeB` according to De Morgan's law.

Second, there was a need to associate an hour range to a day and a person to these hour ranges. A new class was created to solve this, it was named __Schedule__. The attributes were the owner of the schedule and a collection of the days with hour ranges. Then, a method to compare to another Schedule object was created. There were two options for the collection of days with their hour ranges: lists (similar to arrays) or dictionary (similar to Hash Maps). A dictionary (key as day, value as HourRange object) was chosen to avoid index searching or several if-else statementes in code (python does not support switch statements).

Next, the logic of the comparison between two Schedule instances was created as a method of Schedule class. This method iterates over dictionary keys (days) of `this` object and check if the `other` object has the same key. If not, it passes, else, it compares if both dictionary values (HourRange) of the same key (day) are overlapping. If there is an overlap, it counts it as a coincidence. This method returns the number of coincidences of two schedules.

Finally, it was known that at least 5 schedules (group of days and hour ranges) are given as an input of the program to be compared each other one time. So, there were unique pairs of schedules that had to be compared avoiding pairs of the same schedule or pairs with the same two schedules but inverted. The function __get_unique_pairs(List of schedules)__ is simple but it allows us to get a list of unique pairs of elements of any kind. This was used in the main function to compare schedules without repeating.

The general program complexity is O(n&#178;).

### Classes

You can see a complete documentation of each class in __[src/util.py](https://github.com/epulla/ioet-exercise/blob/main/src/util.py)__:

- class HourRange:
    + A class used to represent a range between hours, contains a start hour and end hour.
    + There is a method called __is_overlapped_with(HourRange other)__ that returns a boolean if an HourRange object is overlapped with another by its range of hours.

- class Schedule:
    + A class used to represent a week schedule of a person, it contains the owner of the schedule and a dictionary of each day of a person.
    + A dictionary was chosen to avoid index searching or several if-else statementes in code (python does not support switch statements)
    + The method called __compare(Schedule other)__ iterates over a Schedule dictionary days. If the other object does not have the day in its dictionary, it passes, else, it compares if the hour ranges of a day are overlapped, if they are, it counts it as a coincidence. This method returns the number of coincidences of a schedule.

### Folder structure

The main code is located in `src` folder. In the root folder, there are a sample .txt file to run the program and a unit testing file called `test.py`.
