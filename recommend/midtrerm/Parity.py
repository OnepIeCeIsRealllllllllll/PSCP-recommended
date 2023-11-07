"""Parity"""
def data():
    """if count 1 = Odd"""
    #odd >>> num %2 != 0
    bit_ = input()
    want = input()
    count = 0
    for _ in bit_:
        if _ == "1":
            count += 1
    if count %2 == 0 and want == "Even":
        bit_ += "0"
    elif count %2 != 0 and want == "Even":
        bit_ += "1"
    elif count %2 == 0 and want == "Odd":
        bit_ += "1"
    elif count %2 != 0 and want == "Odd":
        bit_ += "0"
    print(bit_)
    print(count)
data()
