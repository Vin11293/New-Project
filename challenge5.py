def only_ints(n, m):
    try:
        n = int(n)
        m = int(m)
        return True
    except ValueError:
        return False
   

n = input("input a character/number")
m = input("input a character/number")
answ = only_ints(n, m)
print ("Are both inputs integers?: ", answ)


