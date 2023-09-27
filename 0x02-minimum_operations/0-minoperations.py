#!/usr/bin/python3
"""
solution to the minimum interview question
"""


from sys import argv


def minOperations(n):
    """
    Calc the fewest number of operations needed to result in exactly n "H" characters in thr file.
    
    
    ::param n: The desired number of 'H' characters.
    :return: The minimum number of operations required.
    """
    
    if n <= 1:
        return 0
    
   
    # Find smallest prime factors
    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i

    return n