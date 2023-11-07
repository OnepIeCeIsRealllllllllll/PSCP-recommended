"""iPad Air"""
def ipad_air(want_color, want_gb, want_internet):
    """buy ipad"""
    color = ("Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue")
    num_gb_store = (64, 256)
    internet = ("Wi-Fi", "Wi-Fi + Cellular")
    price = 0
    if want_color in color and want_gb in num_gb_store and want_internet in internet:
        if want_gb == 64:
            if want_internet == "Wi-Fi":
                price += 19900
            elif want_internet == "Wi-Fi + Cellular":
                price += 24400
        if want_gb == 256:
            if want_internet == "Wi-Fi":
                price += 24900
            elif want_internet == "Wi-Fi + Cellular":
                price += 29400
        print(price)
    else:
        print("Not Available")

ipad_air(input(), int(input()), input())
