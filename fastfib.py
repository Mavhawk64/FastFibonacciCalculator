#Define f as the list of each Fibonacci Number to a given index.
f = [0, 1]

# Function: Fibonacci
# This function appends all of the numbers of the Fibonacci sequence
# to a given index, n.
# n - Passed in index of Fibonacci Sequence.
# returns The Fibonacci Number at that index, n.
def Fibonacci(n):
    #Check to see if n is the length of the array (next index).
    if n == len(f):
        #Append the next Fib Num.
        f.append(f[n-1] + f[n-2])
    #Check if n is larger than the length of the array (outside of the range of the numbers).
    elif n > len(f):
        #Define a to be the length of f (the next index).
        a = len(f)
        #While we haven't reached our needed index...
        while a <= n:
            #Append each Fibonacci Number until we reach the needed index.
            f.append(f[a - 1] + f[a - 2])
            #Iterate a by 1.
            a = a + 1
    return f[n]

# TESTER CODE
# print(Fibonacci(1000))

# for x in range(0, 101):
#     print(Fibonacci(x))
