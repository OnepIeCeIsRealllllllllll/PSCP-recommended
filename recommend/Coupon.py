"""Coupon"""
def satoshi():
    """who win"""
    price = float(input())
    coupon_1 = input().split()
    coupon_2 = input().split()
    cou1_calculate = []
    cou2_calculate = []#รองรับค่าที่appendเข้าไปใหม่
    for i in coupon_1:
        cou1_calculate.append(float(i))
    for j in coupon_2:
        cou2_calculate.append(float(j))
    discount_a = cou1_calculate[0]
    buy_b = cou1_calculate[1]
    discount_x = cou2_calculate[0]
    buy_y = cou2_calculate[1]


    if price >= buy_b:
        result1 = calculator_type1(price, discount_a)
    elif price < buy_b:
        result1 = price
    if price >= buy_y:
        result2 = calculator_type2(price, discount_x)
    elif price < buy_y:#ราคาไม่ถึงขั้นต่ำ
        result2 = price

    print_result(result1, result2, buy_b, buy_y, price)

def print_result(result1, result2, buy_b, buy_y, price):
    """print result and check condition"""
    if result1 < result2:# เราเอาที่ลดแล้วถูกที่สุด ต้องเป็น <
        print("1 %.1f" % result1)
    elif result1 > result2:
        print("2 %.1f" % result2)
# เอา nope case ขึ้นก่อน ขั้นต่ำ เพราะ ตั้งค่าresult ว่าเป็นprice ตอนที่ใช้คูปองไม่ได้
    elif result1 == price and result2 == price:
        print("Nope")
    elif result1 == result2:
        if buy_b <= buy_y:
            print("1 %.1f" % result1)
        elif buy_y < buy_b:
            print("2 %.1f" % result2)

def calculator_type1(price, discount_a):
    """coupon type 1"""
    discount_real1 = price - discount_a
    return discount_real1

def calculator_type2(price, discount_x):
    """calculator type 2"""
    discount_real2 = (price - (price * discount_x / 100))
    return discount_real2

satoshi()
