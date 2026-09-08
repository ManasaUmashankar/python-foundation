# *args - multiple positional arguments
def add_numbers(*numbers):
    total = sum(numbers)
    return total


print("Total:", add_numbers(10, 20, 30))
print("Total:", add_numbers(5, 10, 15, 20))


# **kwargs - multiple keyword arguments
def user_profile(**details):
    print("User Profile:")
    print(details)


user_profile(
    name="Manasa",
    role="SOC Analyst",
    age=19,
    location="India"
)

----

▶️ Expected output
Total: 60
Total: 50
User Profile:
{'name': 'Manasa', 'role': 'SOC Analyst', 'age': 19, 'location': 'India'}
