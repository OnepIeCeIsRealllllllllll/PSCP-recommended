"""chachacha"""
def cha():
    """cha"""
    import math
    day = int(input())
    count = 0
    for _ in range(day):
        hour = float(input())
        count += math.ceil(hour)
    money = count * 8720
    print(int(money))

cha()
