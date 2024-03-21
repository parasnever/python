def bill_total(bill):
    total = 0.00
    for k , v in bill.items():
        total +=v
    return total

def calculate_tax(percent, bill_total):
    return round((percent * bill_total) / 100.0 , 2)

food_bill= {
    1: 3,
    2:5,
    3:6,
    4:9,
    5:8

}

food_total =bill_total(food_bill)
tax_total = calculate_tax(15,food_total)

print("Overall: ",food_total + tax_total)
