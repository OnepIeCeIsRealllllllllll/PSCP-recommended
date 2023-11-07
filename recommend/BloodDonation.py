"""BloodDonation"""
def blood():
    """recommend"""
    ages = int(input())
    weight = int(input())
    times = int(input())

    if ages == 17 or 60 <= ages <= 70:
        agree = input()
    if ages == 17:
        if weight >= 45 and agree == "True":
            return "Yes"
        else:
            return "No"

    elif 18 <= ages < 60:
        if times == 0 and ages <= 55 and weight >= 45 or times != 0 and weight >= 45:
            return "Yes"
        else:
            return "No"

    elif 60 <= ages <= 70:
        if times != 0 and weight >= 45 and agree == "True":
            return "Yes"
        else:
            return "No"
    else:
        return "No"

print(blood())
