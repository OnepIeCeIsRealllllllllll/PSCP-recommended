"""Fever"""
def fever(cel):
    """cold or flu"""
    if 36 <= cel < 38:
        return "No Fever"
    elif 38 <= cel < 39:
        return "Mild Fever"
    elif 39 <= cel < 40:
        return "High Fever"
    elif cel >= 40:
        return "Very High Fever"

print(fever(float(input())))
