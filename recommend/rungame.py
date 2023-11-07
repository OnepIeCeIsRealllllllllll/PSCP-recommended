"""RunGame"""
def rungame():
    """CookieRun"""
    start = 0 #เริ่มต้นที่ 0
    now = 0 #รับมาเก็บค่า
    run = input().split()
    for i in run:
        now += abs(int(i)-start)# int(i) บรรทัดนี้ loop ก่อนตัว start = int(i)
        #เพราะเขยิบเเล้วต้องresetค่า start ใหม่
        start = int(i)
    #     print(i)
    # print(run)
    print(now)
rungame()
