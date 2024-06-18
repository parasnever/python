print(0)
print(1)
count = 2
def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newfibo = prev1 + prev2
        print(newfibo)
        prev2 = prev1
        prev1 = newfibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return
fibonacci(1,0)
#using the recursion of the fibonacci problem