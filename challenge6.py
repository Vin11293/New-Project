def double_letters(string):
    for i in range (len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False
    
result = input("enter word/sentence")
print (double_letters(result))
