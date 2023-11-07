"""Math for IT"""
def math():
    """Math for IT"""
    import math as m
    raduis = float(input())
    area = m.pi * (raduis) ** 2
    cir = 2 * m.pi * raduis
    print("Area: %.3f" %area)
    print("Circumference: %.3f" %cir)

math()
