
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items,end = ' ')

def square(num):
    return num * 2

new_data = map(square, data)

print(new_data)