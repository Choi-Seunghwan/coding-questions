#!/bin/python3

import math
import os
import random
import re
import sys



from datetime import datetime

#
# Complete the 'reformatDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#

def reformatDate(dates):
    # Write your code here
    reformated_results = []

    for date in dates:
        day, month, year = date.split()
        day = day[:-2]
        reformatDate = datetime.strptime(' '.join([day, month, year]) , '%d %b %Y' )
        reformated_results.append(str(reformatDate).split()[0])

    return reformated_results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dates_count = int(input().strip())

    dates = []

    for _ in range(dates_count):
        dates_item = input()
        dates.append(dates_item)

    result = reformatDate(dates)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
