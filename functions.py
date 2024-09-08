def capital_indexes(string):
    caps = []
    for i in range(len(string)):           
        if (string[i].isupper()):
            caps.append(i)
    return caps

cap = capital_indexes(str(input("please input string")))
print(cap)        
