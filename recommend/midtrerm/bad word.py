"""bad word"""
def charge():
    """change o and O to i and I"""
    word = input()#เปลี่ยนจาก o เป็น i
    data = ""
    for i in word:
        if i != "o" and i != "O":
            data+=i
        if i == "o":
            data+="i"
        if i == "O":
            data+="I"
    print(data)
charge()
