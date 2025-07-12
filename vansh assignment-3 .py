#assignment - 3
# task - 1

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*= i
    return result

num=int(input("Enter a number: "))
print(f"factorial of {num} is:{factorial(num)}")



# task - 2
import math
num=float(input("Enter a number: "))
sqrt_val=math.sqrt(num)
log_value=math.log(sqrt_val)
sin_value=math.sin(log_value)
print(f"sqrt of {num} is:{sqrt_val}")
print(f"logarithm of {num} is:{log_value}")
print(f"sinh of {num} is:{sin_value}")

