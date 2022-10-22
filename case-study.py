import sys
from collections import deque


# STACKS
def stacks():
    stack_list = []

    # PUSH METHOD
    print('\n\nStack PUSH Method')
    stack_len = int(input('\nEnter your desired number of stack: '))
    i = len(stack_list)

    while i != stack_len:
        stack_list.append(int(input('Enter a number on stack: ')))
        i += 1

    print('\nItems on stack')
    print(stack_list)

    # POP METHOD
    print('\n\nStack POP Method')
    while i > 0:
        j = input('\nRemove a number in stack? (Y/N): ')
        if j == 'Y':
            stack_list.pop()
            print(stack_list)
        else:
            print(stack_list)
            break
        i -= 1
    if i == 0:
        print("Stack is now empty")

    x = input('\nTry again(Y) or Exit(N)?: ')
    if x == 'Y':
        stacks()
    else:
        return -1


# QUEUES
def queues():
    queue_list = []

    # ENQUEUE
    print('\n\nENQUEUE Method')
    queue_len = int(input('\nEnter your desired number of queue: '))
    i = len(queue_list)

    while i != queue_len:
        queue_list.append(int(input('Enter a number on queue: ')))
        i += 1

    print("\nItems on queue")
    print(queue_list)

    # DEQUEUE
    print('\n\nDEQUEUE Method')
    queue_list = deque(queue_list)
    while i > 0:
        j = input('Remove a number in queue? (Y/N): ')
        if j == 'Y':
            queue_list.popleft()
            print(queue_list)
        else:
            print(queue_list)
            break
        i -= 1
    if i == 0:
        print('Queue is now empty')

    x = input('\nTry again(Y) or Exit(N)?: ')
    if x == 'Y':
        queues()
    else:
        return -1


# Input number
def input_num(x):
    print('\nEnter 10 values')
    for i in range(1, 11):
        x.insert(i, int(input('Enter input {}: '.format(i))))


def linear_search_algorithm(list_search, m, find_num):
    for i in range(0, m):
        if list_search[i] == find_num:
            return i
    return -1


# Linear Search
def linear_search():
    search_list = []
    print('\n\nLinear Search')
    input_num(search_list)
    print('\n')
    print(search_list)
    num_find = int(input('\nEnter a number you want to find: '))
    n = len(search_list)
    result = linear_search_algorithm(search_list, n, num_find)

    if result != -1:
        print('\nNumber {} found at index {}'.format(num_find, result))
    else:
        print('\nNumber {} not found'.format(num_find))

    x = input('\nTry again(Y) or Exit(N)?: ')
    if x == 'Y':
        linear_search()
    else:
        return -1


# Binary Search
def binary_search_algorithm(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_algorithm(array, element, start, mid - 1)
    else:
        return binary_search_algorithm(array, element, mid + 1, end)


def binary_search():
    search_list = []
    print('\n\nBinary Search')
    input_num(search_list)
    print('\n')
    print(search_list)
    num_find = int(input('\nEnter a number you want to find: '))
    n = len(search_list)
    result = binary_search_algorithm(search_list, num_find, 0, n)

    if result != -1:
        print('\nNumber {} found at index {}'.format(num_find, result))
    else:
        print('\nNumber {} not found'.format(num_find))

    x = input('\nTry again(Y) or Exit(N)?: ')
    if x == 'Y':
        binary_search()
    else:
        return -1


# BUBBLE SORT
def bubble_sort(sorting_list):
    for i in range(0, len(sorting_list) - 1):
        for j in range(0, len(sorting_list) - i - 1):
            if sorting_list[j] > sorting_list[j + 1]:  # sorting_list[j] < sorting_list[j + 1] (descending)
                sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]


# SELECTION SORT
def selection_sort(sorting_list):
    for i in range(0, len(sorting_list) - 1):
        min_index = i
        for j in range(i + 1, len(sorting_list)):
            if sorting_list[j] < sorting_list[min_index]:  # sorting_list[j] > sorting_list[min_index] (descending)
                min_index = j
        if min_index != i:
            sorting_list[i], sorting_list[min_index] = sorting_list[min_index], sorting_list[i]


# SHELL SORT
def shell_sort(sort_list, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = sort_list[i]
            j = i
            while j >= interval and sort_list[j - interval] > temp:  # < temp (descending)
                sort_list[j] = sort_list[j - interval]
                j -= interval

            sort_list[j] = temp
        interval //= 2


# INSERTION SORT
def insertion_sort(sorting_list):
    for i in range(1, len(sorting_list)):
        cur_num = sorting_list[i]
        k = 0
        for j in range(i - 1, -2, -1):
            k = j
            if sorting_list[j] > cur_num:  # sorting_list[j] < cur_num (descending)
                sorting_list[j + 1] = sorting_list[j]
            else:
                break
        sorting_list[k + 1] = cur_num


# MERGE SORT
def merge_sort(x):
    merge_sort2(x, 0, len(x) - 1)


def merge_sort2(x, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(x, first, middle)
        merge_sort2(x, middle + 1, last)
        merge(x, first, middle, last)


def merge(x, first, middle, last):
    left = x[first:middle + 1]
    right = x[middle + 1:last + 1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i = j = 0

    for k in range(first, last + 1):
        if left[i] <= right[j]:
            x[k] = left[i]
            i += 1
        else:
            x[k] = right[j]
            j += 1


# QUICK SORT
def partition(x, low, high):
    pivot = x[high]
    i = low - 1

    for j in range(low, high):
        if x[j] <= pivot:  # x[j] >= pivot (descending)
            i = i + 1
            (x[i], x[j]) = (x[j], x[i])

    (x[i + 1], x[high]) = (x[high], x[i + 1])

    return i + 1


def quick_sort(x, low, high):
    if low < high:
        pi = partition(x, low, high)
        quick_sort(x, low, pi - 1)
        quick_sort(x, pi + 1, high)


# Sorting Algorithms
def sorting_algorithms():
    while True:
        print('1 - Bubble Sort')
        print('2 - Selection Sort')
        print('3 - Shell Sort')
        print('4 - Insertion Sort')
        print('5 - Merge Sort')
        print('6 - Quick Sort')
        print('7 - Exit')
        choice = input("\nChoose a Sorting Algorithm: ")

        if choice == '7':
            return -1

        sorting_list = []
        input_num(sorting_list)
        print('\nOriginal values')
        print(sorting_list)
        quicksort_size = len(sorting_list) - 1
        size = len(sorting_list)
        if choice == '1':
            bubble_sort(sorting_list)
            break
        elif choice == '2':
            selection_sort(sorting_list)
            break
        elif choice == '3':
            shell_sort(sorting_list, size)
            break
        elif choice == '4':
            insertion_sort(sorting_list)
            break
        elif choice == '5':
            merge_sort(sorting_list)
            break
        elif choice == '6':
            quick_sort(sorting_list, 0, quicksort_size)
            break
        else:
            print('Enter a correct number!!!')

    print("\nSorted Values")
    print(sorting_list)

    x = input('\nTry again(Y) or Exit(N)?: ')
    if x == 'Y':
        sorting_algorithms()
    else:
        return -1


while True:
    print('\n\n\n********** Data Structures and Algorithms: Case Study **********')
    print('1 - Stacks')
    print('2 - Queues')
    print('3 - Linear Search')
    print('4 - Binary Search')
    print('5 - Sorting Algorithms')
    print('6 - Exit')
    menu_choice = input("\nEnter a number of your choice: ")

    if menu_choice == '1':
        stacks()
    elif menu_choice == '2':
        queues()
    elif menu_choice == '3':
        linear_search()
    elif menu_choice == '4':
        binary_search()
    elif menu_choice == '5':
        sorting_algorithms()
    elif menu_choice == '6':
        exit()
    else:
        print('Enter a correct number!!!')
