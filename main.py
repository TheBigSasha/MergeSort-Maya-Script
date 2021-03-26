# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import all the modules
import maya.cmds as cmds
import random
import copy


class MergeSortArgs:
    def __init__(self, array, left_index, right_index):
        self.array = copy.deepcopy(array)
        self.left_index = left_index
        self.right_index = right_index

    def __str__(self):
        arr = ""
        for inst in self.array:
            arr = arr + str(inst) + ", "
        return str.format("array: {}, left_index: {}, right_index: {}", arr, self.left_index, self.right_index)


class MergeArgs:
    def __init__(self, array, left_index, right_index, middle):
        self.array = copy.deepcopy(array)
        self.left_index = left_index
        self.right_index = right_index
        self.middle = middle

    def __str__(self):
        arr = ""
        for inst in self.array:
            arr = arr + str(inst) + ", "
        return str.format("array: {}, left_index: {}, right_index: {}, middle: {}", arr, self.left_index,
                          self.right_index, self.middle)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return str.format("{}", self.year)


def merge(array, left_index, right_index, middle, comparison_function):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle + 1:right_index + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # We use the comparison_function instead of a simple comparison operator
        if comparison_function(left_copy[left_copy_index], right_copy[right_copy_index]):
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(array, left_index, right_index, comparison_function):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle, comparison_function)
    yields.append(MergeSortArgs(array, left_index, middle))
    merge_sort(array, middle + 1, right_index, comparison_function)
    yields.append(MergeSortArgs(array, middle + 1, right_index))
    merge(array, left_index, right_index, middle, comparison_function)
    yields.append(MergeArgs(array, left_index, right_index, middle))


car1 = Car("Alfa Romeo", "33 SportWagon", 1988)
car2 = Car("Chevrolet", "Cruze Hatchback", 2011)
car3 = Car("Corvette", "C6 Couple", 2004)
car4 = Car("Cadillac", "Seville Sedan", 1995)
car5 = Car("Cadillac", "Seville Sedan", 2333)
car6 = Car("Cadillac", "Seville Sedan", 112)
car7 = Car("Cadillac", "Seville Sedan", 33)
car8 = Car("Cadillac", "Seville Sedan", 3123)

yields = []
array = [car1, car2, car3, car4, car5, car6, car7, car8]
merge_sort(array, 0, len(array) - 1, lambda carA, carB: carA.year < carB.year)
for i in yields:
    print(i)
