"""Brick Bridge"""
def main(small, big, goal):
    """Brick Bridge"""
    needb = goal // 5
    useb = min(big, needb)
    left = goal - useb * 5
    if left > small:
        print(-1)
    else:
        print(left)

main(int(input()), int(input()), int(input()))
