"""RockPaperScissor"""
def winwin():
    """RockPaperScissor"""
    # string slicing in python
    game = input()
    in_a = 0
    in_b = 0
    for i in range(0, len(game), 2):
        count = game[i]+game[i+1]
        if count == "RS" or count == "PR" or count == "SP":
            in_a += 1
        elif count == "SR" or count == "RP" or count == "PS":
            in_b += 1
    if in_a > in_b:
        print("A win %s-%s" %(in_a, in_b))
    elif in_b > in_a:
        print("B win %s-%s" %(in_b, in_a))
    elif in_a == in_b:
        print("DRAW %d" %in_a)

winwin()
