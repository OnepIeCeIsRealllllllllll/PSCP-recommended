"""Grade III"""
def grade():
    """Grade III"""
    import math
    subject = int(input())
    total = 0
    for _ in range(subject):
        order = float(input())
        if order >= 95 and order <= 100:
            total += 4
        elif order >= 90:
            total += 3.5
        elif order >= 85:
            total += 3
        elif order >= 80:
            total += 2.5
        elif order >= 75:
            total += 2
        elif order >= 70:
            total += 1.5
        elif order >= 65:
            total += 1
        elif order >= 60:
            total += 0.5
        else:
            total += 0
    print("%.2f" % (math.floor((total / subject)*100)/100))
# *ใช้ int() แทนการimport floor ได้

grade()
