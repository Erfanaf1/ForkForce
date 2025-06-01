def custom_math_operation(number):
    if number % 2 == 0:
        return number * 2
    else:
        return number * 3

num = 7
result = custom_math_operation(num)
print(f"The result is: {result}")
