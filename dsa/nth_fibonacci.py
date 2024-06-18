def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1)+ F(n-2)

print(F(19))
#nth fibonaci using the formulap