""" OTP"""
def main():
    """OTP"""
    all_otp = []
    count_1 = 0
    count_34 = 0
    count_6 = 0

    while True:
        otp = input()
        all_otp.append(otp)
        lenotp = len(all_otp)
        if "0" in all_otp:
            all_otp.pop()
            break

    if lenotp == 4 and (count_1 == 1 or count_34 == 1):
        print("Valid")
    elif lenotp == 6 and (count_1 == 2 or count_34 == 1):
        print("Valid")
    elif lenotp == 8 and (count_1 == 3 or count_34 == 2 or count_6 == 1):
        print("Valid")
    else:
        print("Invalid")
main()
