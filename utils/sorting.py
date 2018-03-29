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

def merge_sort(input_array):
    def m_sort(input_array, left, right):
        array = input_array
        if right - left > 1:
            middle = (left + right) // 2
            left_part = m_sort(array, left, middle)
            right_part = m_sort(array, middle, right)
            i = left
            k = 0
            j = 0

            while (k < len(left_part)) and (j < len(right_part)):
                if left_part[k] < right_part[j]:
                    array[i] = left_part[k]
                    k += 1
                else:
                    array[i] = right_part[j]
                    j += 1
                i += 1

            while k < len(left_part):
                array[i] = left_part[k]
                i += 1
                k += 1

            while j < len(right_part):
                tt = right_part[j]
                array[i] = tt
                i += 1
                j += 1

            return array[left:right]

        else:
            return array[left:right]
    return m_sort(input_array, 0, len(input_array))
