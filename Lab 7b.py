# Name: Carmen Huff
# Course: IT-1051 - Introduction to Programming
# Lab: Lab 7b

# Problem 1 - Restaurant Tip Calculator

bills = [25.00, 48.50, 75.00, 120.00, 42.50]

total_tip = 0

for bill in bills:

    if bill <= 50:
        tip_rate = 0.15
    else:
        tip_rate = 0.20

    tip_amount = bill * tip_rate
    final_total = bill + tip_amount

    print("Bill: $", format(bill, ".2f"))
    print("Tip Rate:", int(tip_rate * 100), "%")
    print("Tip Amount: $", format(tip_amount, ".2f"))
    print("Final Total: $", format(final_total, ".2f"))
    print()

    total_tip += tip_amount

print("Total Tips Earned: $", format(total_tip, ".2f"))
