"""foodgrade"""
def chicken(num, counting):
    if num <= 24:
        weight_meat = int(input())
        counting = compare_meat(weight_meat, counting)
        chicken(num + 1, counting)
    else: 
        print(counting)
        
def compare_meat(weight, counter):
    if weight >=50 and weight <= 70:
        return counter + 1
    else:
        return counter

chicken(1, 0)
