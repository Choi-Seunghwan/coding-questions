import random

arr = [random.randint(0, 100) for k in range(20)]

def qSort(arr):
    if len(arr) == 0:
        return []
    pivot = arr[int(len(arr)/2)]
    lArr = []
    mArr = []
    rArr = []
  
    for i in arr:
        if i < pivot:
            lArr.append(i)
        elif i > pivot:
            rArr.append(i)
        else:
            mArr.append(i)
    return qSort(lArr) + mArr + qSort(rArr)
  
arr = [9, 5, 6, 4, 2, 7, 8, 1, 3]
print(qSort(arr))