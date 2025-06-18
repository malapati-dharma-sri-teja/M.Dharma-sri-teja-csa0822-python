n = int(input("Enter number of items: "))
total = 0

for i in range(n):
    name = input("Item name: ")
    price = float(input("Price: ₹"))
    qty = int(input("Quantity: "))
    total += price * qty

print(f"\nTotal Bill: ₹{total:.2f}")

