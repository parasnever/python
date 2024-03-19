# with open('python/newfile.txt', 'w') as file:
#     # file.write("This is a new file created.")
#     file.writelines(["this is a file.", "\n this is a another file."])
try:
    with open('sample/newfile.txt', 'a') as file:
        file.writelines(["\nthis is first line2", " \n this is second line"])
except FileNotFoundError as e:
    print("error",e)
