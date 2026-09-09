# Multiple Return Values

def user_details():
    name = "Manasa"
    role = "SOC Analyst"
    age = 19

    return name, role, age


# Receive multiple returned values
name, role, age = user_details()

print("Name:", name)
print("Role:", role)
print("Age:", age)

-----

▶️ Expected Output
Name: Manasa
Role: SOC Analyst
Age: 19
