

def factorial(total, n):
    if n == 0:
        print(total)
        return
    else:
        total *= n
        factorial(total, n-1)
        

num = int(input())
result = 1

factorial(result, num)

