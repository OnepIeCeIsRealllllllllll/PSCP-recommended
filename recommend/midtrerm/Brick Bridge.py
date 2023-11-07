"""Brick Bridge"""
def bridge(small, big, goal):
    """use 5 and then use 1"""
    needb = goal // 5 #ใช้ก้อนใหญ้กี่ก้อน
    useb = min(big, needb)
    left = goal - useb * 5
    if left > small:
        print(-1)
    else:
        print(left)

bridge(int(input()), int(input()), int(input()))
