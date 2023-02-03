import time
import random
random.seed(10)

def int_list():
    result = []
    for i in range(0, 5000):
        result.append(random.randint(1, 1000))

    return result

def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                swapped = True
        if not swapped:
            break
    return data

def avg_bubble_sort_time(data, iterations):
    _time = 0
    for it in range(iterations):
        st_time = time.time()
        bubble_sort(data)
        __time = time.time() - st_time
        print(it+1, __time)
        _time += __time

    return _time/iterations

def avg_bubble_sort_time2(iterations):
    _time = 0
    for it in range(iterations):
        data = int_list()
        st_time = time.time()
        bubble_sort(data)
        __time = time.time() - st_time
        print(it+1, __time)
        _time += __time

    return _time/iterations


print('Average time from task: ', avg_bubble_sort_time(int_list(), 5))
print('****************************************')
print('Real Average time: ', avg_bubble_sort_time2(5))