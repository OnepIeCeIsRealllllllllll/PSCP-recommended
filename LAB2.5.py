class ArrayStack:
    """."""
    def __init__(self):
        """."""
        self.size = 0
        self.data = []
    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def is_empty(self):
        """."""
        if self.size <= 0:
            return True
        else:
            return False
    def pop(self):
        """ลบข้อมูลที่อยู่ส่วน Top ของ Stack"""
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return "None"
        else:
            last = self.data[-1]
            self.data.pop()
            self.size -= 1
            return last
    def get_stack_top(self):
        """คืนค่า ข้อมูลที่อยู่ส่วน Top ของ Stack"""
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return "None"
        else:
            return self.data[-1]
    def get_size(self):
        """คืนค่า จำนวนเต็มที่บอกขนาดหรือจำนวนข้อมูลใน Stack"""
        return self.size
     
    def print_stack(self):
        """พิมพ์ข้อมูลใน Stack"""
        return print(self.data)
def is_parentheses_matching():
    """จับคู่ ( และ )"""
    stack_l = ArrayStack()
    stack_r = ArrayStack()
    stack_tmp = ArrayStack()
    #pop = "None"
    expression = input()
    for i in expression:
        if i == '(':
            stack_l.push(i)
            stack_tmp.push(i)
        elif i == ')':
            # pop = stack_tmp.pop()
            # if pop == "None":
            #     break
            stack_tmp.pop()
            stack_r.push(i)
    if stack_l.size == stack_r.size and stack_tmp.is_empty():
        print("Parentheses in", expression, "are matched")
        return True
    else:
        print("Parentheses in", expression, "are unmatched")
        return False
print(is_parentheses_matching())