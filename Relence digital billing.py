listofitem = ("Laptop", "Mobile", "Headphone")
a = float(input("Enter the price of Laptop ----> "))
b = float(input("Enter the price of Mobile ----> "))
c = float(input("Enter the price of Headphone ----> "))

# Safety Checks
if a < 0 or b < 0 or c < 0:
    print("Error: Price cannot be negative!")
    exit()

bill = a + b + c

# Initial Setup (This was the error line - now fixed!)
saved = 0
final_price = bill

print("Your total bill is: " + str(bill))

# The Discount Chain
if bill > 50000:
    discount = 0.10 * bill
    saved = discount
    final_price = bill - discount
    print("Congrats! You got a 10% Discount.")
    
elif 20000 <= bill <= 50000:
    discount1 = 0.05 * bill  # 5% is 0.05
    saved = discount1
    final_price = bill - discount1
    print("Congrats! You got a 5% Discount.")

# Final Bill Printing
print(f"Total Bill: ₹{bill}")
print(f"You Saved: ₹{saved}")
print(f"Final Price to Pay: ₹{final_price}")

