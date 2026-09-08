# Day 1 - Default Parameters

def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price


# With a discount
print("20% discount:", calculate_discount(1000, 20))

# Without specifying a discount
print("Default discount:", calculate_discount(1000))

---
▶️ Expected output
20% discount: 800.0
Default discount: 900.0
