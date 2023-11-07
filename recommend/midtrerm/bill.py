"""bill"""
def bill():
    """bill"""
    food = int(input())
    service = (food * 10)/100
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    real_foodservice = food + service
    vat = (real_foodservice * 7) / 100
    total = real_foodservice + vat
    print("%.2f"%total)

bill()
