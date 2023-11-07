# def pongya(num):
#     """make dicision what I'm gonna say"""
#     if num%3 == 0 or str(num)[-1] == "3":
#         print("PONG")
#     else:
#         print(num)
# pongya(int(input()))




# """[Recommended] Dart"""
# def dart():
#     """circle 5 limit"""
#     num = int(input())
#     new = []
#     score = 0
#     for i in range(num):
#         point = input().split()
#         new.append(point)
#     for j in range(len(new)):
#         point_x = int(new[j][0])
#         point_y = int(new[j][1])
#         score += xxx(score, point_x, point_y)
#         score += yyy(score, point_x, point_y)
    
#     print(score)

# def xxx(score, point_x, point_y):
#     score = 0
#     if point_x > 0 or point_x >= point_y:#x_point
#         if 0 <= point_x <= 2:
#             score += 5
#         elif 2 < point_x <= 4:
#             score += 4
#         elif 4 < point_x <= 6:
#             score += 3
#         elif 6 < point_x <= 8:
#             score += 4
#         elif 8 < point_x <= 10:
#             score += 1
#         else:
#             score += 0
#         return score

# def yyy(score, point_x, point_y):
#     score = 0
#     if point_y > 0 or point_y > point_x:
#         if 0 <= point_y <= 2:
#             score += 5
#         elif 2 < point_y <= 4:
#             score += 4
#         elif 4 < point_y <= 6:
#             score += 3
#         elif 6 < point_y <= 8: 
#             score += 4
#         elif 8 < point_y <= 10:
#             score += 1
#         else:
#             score += 0
#     return score

# def equl():
#     if point_x == point_y:
# dart()

# gam = ["max", "dear", "plia", "pure", "chompo"]
# for i in range(len(gam)):
#     print(i)

#     """pro"""
# def pro(pro_eat, pay, price, eat):
#     """same donut"""
#     pre_pay = eat // pro_eat
#     real_pay = eat - pre_pay
#     real_price = real_pay * price
#     print(real_price)

# pro(int(input()), int(input()), int(input()), int(input()))


# """RunGame"""
# def main(all_dis):
#     """RunGame"""
#     distance = all_dis.split()
#     data = 0
#     now_point = 0
#     for i in distance:
#         data += abs(int(i) - now_point)
#         now_point = int(i)
#     print(data)

# main(input())

# def main():
#     data = {}
#     data["I  here"] = "Gam"
#     data["Guu"] = "Aun"
#     data["Guu"] = "kuy"
#     print(data)
# main()

