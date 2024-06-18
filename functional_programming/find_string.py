def ispresent(person):
    names = ["ram",'shyam',"hari","N7"]
    if person in names:
        return True

    else:
        return False


def nodigit():
    if person.isalpha():
        return True

    else: 
        return False

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)

def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11)

# for x in range(1, 4):
#     print(int((str((float(x))))))

class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())