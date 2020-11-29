#!/bin/python3

import math
import os
import random
import re
import sys


import math

#
# Complete the 'protectionTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY startingPos
#  2. INTEGER_ARRAY speed
#

def protectionTime(startingPos, speed):
    # Write your code here
    sec = 1
    goal_times = []

    for i in range(len(startingPos)):
        goal_times.append( math.ceil(startingPos[i] / speed[i]) )
    
    goal_times.sort()

    # for i in range(len(startingPos)):
    #     goal_times.remove(min(goal_times))
    #     if sec in goal_times or len(goal_times) == 0:
    #         return sec 
    #     sec += 1
    
    for i in range(0, len(goal_times)):
        if sec > goal_times[i]:
            return goal_times[i]
        sec += 1

    return goal_times[-1]
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    startingPos_count = int(input().strip())

    startingPos = []

    for _ in range(startingPos_count):
        startingPos_item = int(input().strip())
        startingPos.append(startingPos_item)

    speed_count = int(input().strip())

    speed = []

    for _ in range(speed_count):
        speed_item = int(input().strip())
        speed.append(speed_item)

    result = protectionTime(startingPos, speed)

    fptr.write(str(result) + '\n')

    fptr.close()
