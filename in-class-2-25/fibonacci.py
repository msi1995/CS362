def fibonacci(int):
    if int >= 0:
        if int==0:              #fib(0) is zero
            return 0
        if int == 1:            #fib(1) is 1
            return 1
        else:
            return fibonacci(int-1) + fibonacci(int-2)




##function for factorial of number
def fact(val):
    factorial = 1
    factorial2 = []
    for i in range(val):
        factorial2.append(i+1)
    
    for i in range(len(factorial2)):
        factorial = factorial2[i] * factorial

    return fact