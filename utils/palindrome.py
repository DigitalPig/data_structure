'''
Use dequeue to test dequeue to find out
'''

from collections import deque

def check_palindrome(string):
    """
    Check if string is a palindrome or not
    """

    string_queue = deque(list(string))

    while len(string_queue) > 1:
        if string_queue.pop() != string_queue.popleft():
            return False

    return True
