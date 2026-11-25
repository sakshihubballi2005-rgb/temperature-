# Discount calculator based on purchase amount

amount = float(input("Enter the purchase amount: "))

if amount >= 15000:
    discount_rate = 20
else:
    discount_rate = 5

discount = amount * discount_rate / 100
final_amount = amount - discount

print(f"Purchase Amount : ₹{amount:.2f}")
print(f"Discount ({discount_rate}%) : ₹{discount:.2f}")
print(f"Final Amount    : ₹{final_amount:.2f}")