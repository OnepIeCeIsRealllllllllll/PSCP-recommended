"""WPM"""
def wpm_input():
    """input"""
    age = input()
    wpm = int(input())
    if age == "Kids":
        kid_ = kid(wpm)
        print(kid_)
    elif age == "Adults":
        adult_ = adult(wpm)
        print(adult_)
    # อย่าลืมตั้งตัวเเปลมารับค่าฟังก์ชัน
 
def kid(wpm):
    """kids wpm"""
    if wpm < 11:
        return "Very Slow"
    elif 11 <= wpm <= 20:
        return "Slow"
    elif 21 <= wpm <= 30:
        return "Average"
    elif 31 <= wpm <= 40:
        return "Fast"
    elif wpm > 40:
        return "Very Fast"
 
def adult(wpm):
    """adults wpm"""
    if wpm < 26:
        return "Very Slow"
    elif 26 <= wpm <= 35:
        return "Slow/Beginner"
    elif 36 <= wpm <= 45:
        return "Intermediate/Average"
    elif 46 <= wpm <= 65:
        return "Fast/Advanced"
    elif 66 <= wpm <= 80:
        return "Very Fast"
    elif wpm > 80:
        return "Insane"
 
wpm_input()