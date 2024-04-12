
total_bill = 210
discount1 = 10
discount2 = 20


if total_bill > 100 and total_bill < 200:
    print("The bill is greater than the 100!")
    total_bill = total_bill - discount1
elif total_bill > 200:
    print("The bill is greater than 200!")
    total_bill =  total_bill - discount2
else:
    print("The bill is less than 100!")


print("The total bill is: " + str(total_bill))
import sys
print(sys.version)