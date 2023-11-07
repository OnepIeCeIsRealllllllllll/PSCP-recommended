"""Heron of Alexandria"""
def tringle():
    """susu"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    av_ = (num1 + num2 + num3)/2

    if av_ - num1 >= 0 and av_ - num2 >= 0 and av_ - num3 >= 0:
        area = (av_*(av_ - num1)*(av_ - num2)*(av_ - num3))**0.5
        print("%.3f" %area)

tringle()
    