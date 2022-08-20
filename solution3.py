# Write code for algorithm 3 below

def nth_fibbonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return nth_fibbonacci(n-1)+nth_fibbonacci(n-2)


print("2nd fib number:")
print(nth_fibbonacci(2))
print("4th fib number:")
print(nth_fibbonacci(4))
print("8th fib number:")
print(nth_fibbonacci(8))

# Write a function tribonacci that takes in a number argument,
# n, and returns the n-th number of the Tribonacci sequence.

# The 0-th and 1-st numbers of the sequence are both 0.

# The 2-nd number of the sequence is 1.

# To generate further numbers of the sequence, calculate the
# sum of previous three numbers.

# Solve this recursively.


def tribonacci(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        return (tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3))


for i in range(2, 10):
    print(tribonacci(i))
