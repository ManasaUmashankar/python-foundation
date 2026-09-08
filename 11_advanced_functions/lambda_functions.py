Lambda Functions

# Normal function
def square(number):
    return number * number


print("Normal function:", square(5))


# Lambda function
square_lambda = lambda number: number * number

print("Lambda function:", square_lambda(5))


# Another example
add = lambda a, b: a + b

print("Addition:", add(10, 20))
------

▶️ Expected Output
Normal function: 25
Lambda function: 25
Addition: 30
