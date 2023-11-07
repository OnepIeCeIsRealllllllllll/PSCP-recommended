# """donut"""
# def main(price_a, donut_b, free_c, want_d):
#     """donut"""
#     set_ = donut_b + free_c
#     n_box = want_d // set_
#     left = want_d % set_
#     if left >= donut_b:
#         n_box += 1
#         left = 0
#     price = (price_a * n_box * donut_b)+(price_a * left)
#     print(price, (set_ * n_box) + left)

# main(int(input()), int(input()), int(input()), int(input()))

def donut(a, b, c, d):
    """donut brooo"""
    box_set = b + c
    box =  d // box_set
    left = d % box_set
    if left >= b:
        box += 1
        left = 0
    price = (a * box * b) + (left * a)
    print(price, (box * box_set) + left)

donut(int(input()), int(input()), int(input()), int(input()))
