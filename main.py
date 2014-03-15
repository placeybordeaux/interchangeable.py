import time
from interchangeable import interchangeable

def fib_recursive(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dynamic(n):
    arr = [1,1]
    while n > 1:
        n -= 1
        arr[n%2] += arr[(n+1)%2]
    return arr[n%2]

if __name__ == "__main__":
    fib = interchangeable(fib_recursive, fib_dynamic)
    start = time.time()
    fib.learning = True
    for i in range(35):
        print fib(i)
    print "took ", time.time() - start, " seconds"
    fib.learning = False
    start = time.time()
    for i in range(35):
        print fib(i)
    print "took ", time.time() - start, " seconds"
    start = time.time()
    for i in range(35):
        print fib_dynamic(i)
    print "took ", time.time() - start, " seconds"
