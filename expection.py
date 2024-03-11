def divide_by(a,b):
    return a / b
try:
    ans = divide_by(40 , 0)
    print(ans)
except ZeroDivisionError as e:
   print(e,"we cannot divide by zero")
except Exception as e:
    print(e,"something went wrong")

#IndexError
try:
    item = items[6]
    print(item)
except: 
    print("The index does not exist in the list.")


#zeroDivisionError
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)

#fileNotFound
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  
