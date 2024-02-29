sample_dic1 = {1: 'coffee', 2: 'tea', 3: 'juice'}
# print(sample_dic1)
# print(sample_dic1[1])
sample_dic1[2] = 'Mint Tea'
print(sample_dic1)
del sample_dic1[3]
print(sample_dic1)

for key, value in sample_dic1.items():
    print(str(key)+ " : "  + str(value))
