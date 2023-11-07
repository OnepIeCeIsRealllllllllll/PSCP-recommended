"""Parity"""
def parity():
    bit_ = input()
    want = input()
    count = 0
    for i in bit_:
        if i == "1":
            count += 1
        print(count)

parity()
