"""Helloooo"""
def long(word):
    """hello"""
    aeiou = ["a", "e", "i", "o", "u"]
    add_on = ""
    for i in word:
        if i in aeiou:
            add_on = i
    index = word.rfind(add_on)#คืนค่าว่าอยู่ตำเเหน่งไหน
    result = word[:index] + (add_on*3) + word[index:]
    print(result)

long(input())
