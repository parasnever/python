def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

str = "I love you"
reverse = string_reverse(str)
print(reverse)