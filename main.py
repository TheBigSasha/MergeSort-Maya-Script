# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import all the modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import maya.cmds as cmds
import matplotlib as mp
import numpy as np
import random


# function to recursively divide the arra
def mergesort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1

    # yield from statements have been used to yield
    # the array from the functions
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)


# function to merge the array
def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i in range(len(merged)):
        A[start + i] = merged[i]
        yield A


# function to plot bars
def showGraph():
    # for random unique values
    n = 20
    a = [i for i in range(1, n + 1)]
    random.shuffle(a)
    datasetName = 'Random'

    # generator object returned by the function
    generator = mergesort(a, 0, len(a) - 1)
    algoName = 'Merge Sort'

    # style of the chart
    plt.style.use('fivethirtyeight')

    # set colors of the bars
    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map",
        {
            "red": [(0, 1.0, 1.0),
                    (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5),
                      (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5),
                     (1.0, 0, 0)]
        }
    )

    fig, ax = plt.subplots()

    # bar container
    bar_rects = ax.bar(range(len(a)), a, align="edge",
                       color=color_map(data_normalizer(range(n))))

    # setting the limits of x and y axes
    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(1.1 * len(a)))
    ax.set_title("ALGORITHM : " + algoName + "\n" + "DATA SET : " + datasetName,
                 fontdict={'fontsize': 13, 'fontweight': 'medium',
                           'color': '#E4365D'})

    # the text to be shown on the upper left
    # indicating the number of iterations
    # transform indicates the position with
    # relevance to the axes coordinates.
    text = ax.text(0.01, 0.95, "", transform=ax.transAxes,
                   color="#E4365D")
    iteration = [0]

    def animate(A, rects, iteration):
        for rect, val in zip(rects, A):
            # setting the size of each bar equal
            # to the value of the elements
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))

    # call animate function repeatedly
    anim = FuncAnimation(fig, func=animate,
                         fargs=(bar_rects, iteration), frames=generator, interval=50,
                         repeat=False)
    plt.show()


showGraph()
