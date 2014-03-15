import time
from math import sqrt 
from interchangeable import interchangeable

def fib_recursive(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dynamic(n):
    arr = [0,1]
    while len(arr) < n + 1:
        arr.append(arr[-1] + arr[-2])
    return arr[n]

def fib_closed_form(n):
    return int(round(1/(sqrt(5))*((1+sqrt(5))/2)**n - (1/(sqrt(5))*((1-sqrt(5))/2)**n)))
    

if __name__ == "__main__":
    fib = interchangeable(fib_closed_form, fib_dynamic)
    start = time.time()
    fib.learning = True
    for i in range(350):
        print fib(i)
    print "took ", time.time() - start, " seconds"
    fib.learning = False
    start = time.time()
    for i in range(350):
        print fib(i)
    print "took ", time.time() - start, " seconds"
    start = time.time()
    for i in range(350):
        print fib_closed_form(i)
    print "took ", time.time() - start, " seconds"
