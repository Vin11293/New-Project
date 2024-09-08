def mid(string):
    length = int(len(string))
    if length%2 == 0:
        letter = ""
    else:
        divi = int(length/2)
        for i in range(len(string)):
            letter = string[divi]
    return letter

word = str(input("enter string"))
func = mid(word)
print (func)
