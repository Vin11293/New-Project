#online status counter
def online_count(statuses):
    counts = 0
    for i, j in statuses.items():
        if j == "online":
            counts = int(counts + 1)
    return counts

statuses = input("enter status dictionary")
status = eval(statuses)
func = online_count(status)
print (func)
