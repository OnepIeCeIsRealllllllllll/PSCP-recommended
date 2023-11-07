# """milk"""
# def milk():
#     """milk"""
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#     kuad = d // a
#     cap = kuad
#     if b != 0:
#         while cap >= b:
#             cap -= b
#             kuad += c
#             cap += c
#     print(kuad)
# milk()

"""milk"""
def milk():
    """loop cap"""
    price = int(input())
    cap_exchange = int(input())
    free = int(input())
    moneyyou = int(input())

    khud = moneyyou // price
    cap = khud
    if cap_exchange != 0:
        while cap >= cap_exchange:
            cap -= cap_exchange #เอาฝาไปเเลกขวด
            cap += free
            khud += free
    print(khud)

milk()
