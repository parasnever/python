#we do the radix sort

my_array = [170,45,75,90,802,24,2,66]
print('Original array:',my_array)
radix_array=[[],[],[],[],[],[],[],[],[],[]]
maxVal =max(my_array)
exp = 1

while maxVal // exp > 0:
    while len(my_array) > 0:
        val = my_array.pop()
        radix_index = (val // exp) % 10
        radix_array[radix_index].append(val)

    for bucket in radix_array:
        while len(bucket) > 0:
            val = bucket.pop()
            my_array.append(val)

    exp *= 10
print("Sorted array: ",my_array)