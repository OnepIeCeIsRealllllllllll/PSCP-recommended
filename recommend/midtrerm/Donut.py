"""donut"""
def donut():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())#want
    set = b + c
    n = d // set #จำนวนกล่อง
    r = d % set
    if r >= b:
        n += 1 #ถ้าเศษมัน >= จำนวนโดนัทในกล่องที่ไม่รวมฟรี ก็ซื้อset คุ้มกว่าซื้อเเยกเพราะได้โดนัทฟรีด้วย
        r = 0 #เราเซ็ทเศษเท่ากับ 0 เพราะซื้อset ไปเเล้ว
    price = (n*a*b) + (r*a) #จำนวนกล่อง*ราคาต่อชิ้น*ชิ้นโดนัท(ไม่*free)
    print(price)
    print((set * n) + r)

donut()
    
    
    
    
    
    
    
# #     a = int(input())#price
# #     b = int(input())#buy
# #     c = int(input())#free
# #     d = int(input())#want
# #     set = b + c
# #     time_buy = d//set
# #     left = d - (set*time_buy) #>>>d%set find left piece
# #     if left >= b:
# #         time_buy += 1
# #         left = 0
# #     price = (a * (time_buy * b)) + (a * left)
# #     print(price, (set*time_buy)+left)

# # donut()