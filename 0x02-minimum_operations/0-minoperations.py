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
    
    #initialize an array to store the minimum operations required for each position
    dp = [0] * (n + 1)
      
    for i in range(2, n + 1):
         dp[i] = float('inf')  # Initialize to positive infinity
    for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                
    return dp[n] if dp[n] != float("inf") else 0

if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))