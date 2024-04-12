
coffes = ['americano','latte','cappuccino', 'machiato','Doppio']

def reverse(str):
    return str[::-1]

reversed_coffes = map(reverse,coffes)

for x in reversed_coffes:
    print(x)