
def fib(n):        
    if n<=1:
        return 0
    if n==2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":    
    n = int(raw_input())
    print("Nth Fibanocci number is {}".format(fib(n)))