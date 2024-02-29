def sum_of(**kwargs):
    sum = 0
    for x , v in kwargs.items():
        sum += v
    return round(sum, 2)
print(sum_of(coffee = 2.99, Tea = 4.55, Juice = 4.67))





employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]

def get_employee(id):
    for employee in employee_list:
        if employee[0] == id:
            return {"id": employee[0], "name": employee[1], "department": employee[2]}

print(get_employee(12458))

