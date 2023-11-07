"""SumOfNumber"""
def sumnum():
    """if num == -1 stop total and print"""
    target = int(input())
    total = 0
    while True:
        num = int(input())
        total += num
        if num == -1:
            print(total + 1)
            break
        if total == target:
            print(total)
            break

sumnum()
