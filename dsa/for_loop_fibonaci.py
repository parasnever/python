prev2 = 0
prev1 = 1
print(prev2)
print(prev1)

for fibo in range(18):
    newfibo = prev1 + prev2
    print(newfibo)
    prev2 = prev1
    prev1 = newfibo


#using yhe for loop to find the fibonacci series