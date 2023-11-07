"""How long"""
def countnum():
    """count len of num"""
    num = abs(int(input()))
    count = 0
    for _ in str(num):
        count += 1
    print(count)

countnum()
