'''
This module is to provide a set of search implementation
'''

def binary_search(array, target):
    '''
    Using the binary search approach to find the target.

    Parameters:
    ------------
    array: input array (need to be ordered)
    target: the target that the search is looking for

    Returns:
    -------------
    Boolean: True if target is in array; False if target is not found
    '''

    left = 0
    right = len(array)
    while left < right and right - left > 1:
        middle = (left + right) // 2
        if array[middle] == target:
            return True
        elif target < array[middle]:
            right = middle
        else:
            left = middle

    if right - left == 1:
        return array[left] == target
