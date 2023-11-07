"""pro"""
def pro():
    """same donut"""
    come = int(input())
    pay = int(input())
    price = int(input())
    people = int(input())
    pro_used = (people // come)*pay#จำนวนคนที่ต้องจ่าย
    total = (pro_used+(people%come))*price
    print(total)
pro()
