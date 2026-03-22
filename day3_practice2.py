# Online Shopping Billing System

product1_price = 250
product2_price = 400
product3_price = 150

qty1 = 2
qty2 = 1
qty3 = 3

# Arithmetic operators
total1 = product1_price * qty1
total2 = product2_price * qty2
total3 = product3_price * qty3

subtotal = total1 + total2 + total3

print("Subtotal =", subtotal)

# Discount calculation using comparison operators
if subtotal >= 1000:
    discount = subtotal * 10 / 100
elif subtotal >= 700:
    discount = subtotal * 5 / 100
else:
    discount = 0

print("Discount =", discount)

# Amount after discount
amount_after_discount = subtotal - discount

# GST calculation
gst = amount_after_discount * 18 / 100

print("GST =", gst)

# Final amount
final_amount = amount_after_discount + gst

print("Final Bill =", final_amount)

# Logical operator for free delivery
if final_amount >= 1000 and qty1 + qty2 + qty3 >= 3:
    print("Free Delivery Eligible")
else:
    print("Delivery Charges Apply")
