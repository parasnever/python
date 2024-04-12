# def sum(n):
#    if n == 1:
#        return 0
#    return n + sum(n-1)

# a = sum(5)
# print(a)


# some = ["aaa", "bbb"]

# #1
# def aa(some):
#    return

# #2
# def aa(some, 5):
#    return

# #3
# def aa():
#    return

# #4
# def aa():
#    return "aaa"


numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)