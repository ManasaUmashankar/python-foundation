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
🧠 What's happening here?

This: return name, role, age
       {returns multiple values as a tuple.}

Then:

name, role, age = user_details()
   {unpacks those values into separate variables.}

its just like:
("Manasa", "SOC Analyst", 19)
       ↓
 name      role        age

it has unpacked the 3 values into 3 separate variables
