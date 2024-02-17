https_status = 400
if https_status == 200 or https_status == 2001:
    print("Success!")
elif https_status == 400:
    print('Bad request')
elif https_status == 404:
    print('Not Found')
elif https_status == 500 or https_status == 501:
    print('server error')
else:
    print('unknown')


match https_status:
    case 200 | 2001:
        print("Match sucess")
    case  400:
        print("Match Bad request")
    case 404:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _:
        print: "Unknown"

str = "Paras"
for item in str:
    print(item)
for i in range(12):
    print('Name....',i)

Name = ['paras','Omkumari','Badal','Barasha']
for items in Name:
    if items == 'susant':
        print('He is my brother: ',items)
        continue
    else:
        print('This is not brother name.',items)


count = 0
while count < len(Name):
    print('My real name is : ',Name[count])
    count += 1
for idx, item in enumerate(Name):
    print(idx,item)
