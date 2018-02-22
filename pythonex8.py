import os
import random
import itertools

low = -30
high = 30

A = [(random.randint(low,high), ) for k in range(30)]


def findTriplets(arr, n):

    found = True
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True



    if (found == False):
        print(" not exist ")


arr = A
n = len(arr)
findTriplets(arr, n)
