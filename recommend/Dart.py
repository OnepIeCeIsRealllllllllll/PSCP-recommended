"""Dart"""
def main():
    """dart"""
    num = int(input())
    total = 0
    for _ in range(num):
        score = input().split()
        score_x = int(score[0])
        score_y = int(score[1])
        soot = ((score_x)**2+(score_y)**2)**0.5
        if 2 >= soot >= 0:
            total += 5
        elif 4 >= soot > 2:
            total += 4
        elif 6 >= soot > 4:
            total += 3
        elif 8 >= soot > 6:
            total += 2
        elif 10 >= soot > 8:
            total += 1
    print(total)
main()
