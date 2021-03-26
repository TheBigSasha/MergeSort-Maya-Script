# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import all the modules
# try:
#     import maya.standalone
#     maya.standalone.initialize()
# except:
#     pass
import maya.cmds as cmds
import copy
import random

timeCtr = 0


class Frame(object):
    count = 0

    def __init__(self, frame_number, array):
        self.frame_number = frame_number
        self.array = copy.deepcopy(array)

    def getcount(self):
        return Frame.count

    def __str__(self):
        return "ANONYMOUS FRAME: NUMBER: " + str(self.frame_number)

    def type(self):
        return "Frame"

    def getarray(self):
        return self.array


class MergeSortFrame(Frame):
    def __init__(self, array, left_index, right_index, frame_number=timeCtr):
        super(MergeSortFrame, self).__init__(frame_number, array)
        self.left_index = left_index
        self.right_index = right_index

    def __str__(self):
        arr = ""
        for inst in self.getarray():
            arr = arr + str(inst) + ", "
        return str.format("array: {}, left_index: {}, right_index: {}", arr, self.left_index, self.right_index)

    def range(self):
        return self.left_index, self.right_index

    def type(self):
        return "MergeSort"


class MergeFrame(Frame):
    def __init__(self, array, left_index, right_index, middle, frame_number=timeCtr):
        super(MergeFrame, self).__init__(frame_number, array)
        self.left_index = left_index
        self.right_index = right_index
        self.middle = middle

    def __str__(self):
        arr = ""
        for inst in self.getarray():
            arr = arr + str(inst) + ", "
        return str.format("array: {}, left_index: {}, right_index: {}, middle: {}", arr, self.left_index,
                          self.right_index, self.middle)

    def range(self):
        return self.left_index, self.right_index

    def type(self):
        return "Merge"


class CubeDescription:
    def __init__(self, size, id):
        self.size = size
        self.id = id

    def __str__(self):
        return str.format("pythongeneratedcube{}", self.id)


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
    global timeCtr
    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle, comparison_function)
    yields.append(MergeSortFrame(copy.deepcopy(array), left_index, middle, timeCtr))
    timeCtr = timeCtr + 30
    merge_sort(array, middle + 1, right_index, comparison_function)
    yields.append(MergeSortFrame(copy.deepcopy(array), middle + 1, right_index, timeCtr))
    timeCtr = timeCtr + 30
    merge(array, left_index, right_index, middle, comparison_function)
    yields.append(MergeFrame(copy.deepcopy(array), left_index, right_index, middle, timeCtr))
    timeCtr = timeCtr + 30


yields = []
cubes = dict()
array = []
for i in range(0, 10):
    array.append(CubeDescription(random.uniform(0.7, 5.0), i))
biggest = -999999999
for i in array:
    if i.size > biggest:
        biggest = i.size

for cube in array:
    cubes[cube.__str__()] = cmds.polyCube(name=cube.__str__(), w=cube.size, h=cube.size, d=cube.size)

merge_sort(array, 0, len(array) - 1, lambda carA, carB: carA.size < carB.size)
for frame in yields:
    arr = frame.getarray()
    for i in range(0, len(arr)):
        posX = i * (biggest + 15)
        objs = cmds.ls(arr[i].__str__())
        obj = objs[0]
        time = frame.frame_number
        cmds.setKeyframe(obj, at='tx', v=posX, t=time)
        print(str(obj) + " " + str(posX) + " " + str(time))
