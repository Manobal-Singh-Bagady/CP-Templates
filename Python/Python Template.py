# Author : MSB
# Version : 1.0.0
# Description : CP Template for Python
# Usage : python3
# Notes : None
# Python Version : 3.10.6
# Python Standard : PEP 8
# Python Libraries : None


# --------------------------- I/O Functions ---------------------------

def lm(num: int = None):
    """Function to take input of a list in one line.

    Args:
        num (int, optional): Number of elements in the list. Defaults to None.
    Returns:
        list: List of integers inputted by the user."""

    if num is None:
        return list(map(int, input().split()))
    else:
        return list(map(int,input().split()))[:num]

def pl(arr: list):
    """
    Function to print a list in one line.

    Args:
        arr (list): List to be printed.
        
    Returns:
        None 
        Just prints the list in one line.
    """

    for i in arr:
        print(i,end=' ')
    print()


# --------------------------- Main Code --------------------------

if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        # Code Begins Here
        pass

