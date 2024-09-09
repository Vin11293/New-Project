def only_ints(n, m):
    try:
        n = int(n)
    except ValueError:
        ans = "False"
    try:
        m = int(m)
    except ValueError:
        ans = "False"
    if type(n) is int and type(m) is int:
        ans = "True"
    else:
        ans = "False"
    return ans

n = input("input a character/number")
m = input("input a character/number")
answ = only_ints(n, m)
print ("Are both inputs integers?: ", answ)
