#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTimes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY time
#  2. INTEGER_ARRAY direction
#

def q_empty(q, index):
    if len(q) > index:
        return False
    else:
        return True

def getTimes(time, direction):
    results = [0] * len(time)
    index = 0
    index_enter = 0
    index_exit = 0

    sec = 0
    q_enter = []
    q_exit = []
    enq_count = 0
    flag = 1

    while True: # one loop == sec
        if time[index] <= sec and enq_count < len(time): #arrive
            for i in range(index, len(time)):
                if time[index] == time[i]:
                    if direction[i] == 1:
                        q_exit.append(i)
                    else:
                        q_enter.append(i)
                    enq_count += 1
                else:
                    index = i
                    break
        else:
            if q_empty(q_exit, index_exit) and q_empty(q_enter, index_enter):
                sec = time[index] -1
        
        if not q_empty(q_exit, index_exit) or not q_empty(q_enter, index_enter): #dequeue
            if flag == 1 and not q_empty(q_exit, index_exit) or q_empty(q_enter, index_enter):
                results[q_exit[index_exit]] = sec
                index_exit += 1
                flag = 1
            else:
                results[q_enter[index_enter]] = sec
                index_enter += 1
                flag = 0
        else:
            flag = 1

        if enq_count >= len(time) and q_empty(q_exit, index_exit) and q_empty(q_enter, index_enter):
            break

        sec += 1
        
    return results



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    time_count = int(input().strip())

    time = []

    for _ in range(time_count):
        time_item = int(input().strip())
        time.append(time_item)

    direction_count = int(input().strip())

    direction = []

    for _ in range(direction_count):
        direction_item = int(input().strip())
        direction.append(direction_item)

    result = getTimes(time, direction)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
