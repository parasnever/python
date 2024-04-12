import random
f_name = input("Type of file name: ")
f =open(f_name)
f_content = f.read()
f_content_list = f_content.split("\n")

f.close()
print(random.choice(f_content_list))