# file = open('python/test.txt', mode='r')
with open('python/test.txt', mode='r') as file:
        data = file.readline()

print(data)

# file.close()