'''
Module to provide the sorting function
'''

def bubble_sort(input_array):
    '''
    Bubble sorting
    '''
    array = input_array.copy()
    for i in range(len(array), 0, -1):
        for j in range(i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array

def selection_sort(input_array):
    '''
    Selection sort
    '''
    array = input_array.copy()
    for i in range(len(array), 0, -1):
        max_pos = 0
        max_value = array[0]
        for j in range(i):
            if array[j] > max_value:
                max_pos = j
                max_value = array[j]
        # Exchange elements
        temp = array[i-1]
        array[i-1] = max_value
        array[max_pos] = temp
    return array

def insert_sort(input_array):
    '''
    Insert sort
    '''
    array = input_array.copy()
    for i in range(len(array) - 1):
        temp = array[i + 1]
        j = i
        while j>=0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = temp
    return array
