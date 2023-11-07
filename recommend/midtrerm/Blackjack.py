"""Blackjack"""
def black1():
    """blackjack"""
    card = int(input())
    count = 0
    for i in range(card):
        var_ = input()
        if var_ == "K" and var_ == "Q" or var_ == "K":
            count += 10
            
    print(count)
black1()

# def black2():
    
