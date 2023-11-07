"""PH"""
def ph_test(var):
    """what is number"""
    if var >= 0 and var <= 14:
        if var < 7:
            print("acidic")
        elif var == 7:
            print("neutral")
        elif var > 7:
            print("akaline")
    else:
        print("error")
ph_test(float(input()))
