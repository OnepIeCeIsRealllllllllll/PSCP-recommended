"""ATM"""
def atm():
    """normal cal"""
    money = int(input())
    money_now = money
    new = []
    while True:
        modern = input()
        # print(modern)
        if "END" == modern:
            break
        new.append(modern.split())
    for i in new:
        # ['D', '20']
        # ['W', '30']
        # ['W', '50']
        if i[0] == "D":
            money_now += int(i[1])
        elif i[0] == "W":
            money_now = check(money_now, int(i[1]))
    print(money_now)
 
def check(money_now, withdraw):
    """check when money"""
    if money_now <= withdraw:
        money_now = 0
    elif money_now > withdraw:
        money_now -= withdraw
    return money_now
 
atm()