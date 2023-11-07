"""Inverter"""
def change():
    """swap case"""
    bit = input()
    data = ""
    for i in bit:
        if i == "0":
            data += "1"
        elif i == "1":
            data += "0"
    if data.count("1") == 0:#ถ้านับเเล้วมีเลข 1 0 ตัว
        print("")
    else:
        print(int(data))

change()
