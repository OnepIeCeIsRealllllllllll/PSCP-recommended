"""Lab 02.03 - Student Groups"""
class ArrayStack:
    """."""
    def __init__(self, group, num):
        """."""
        self.group = int(group)
        self.num = int(num)
        self.all = []
        self.newlist = []
    def push(self):
        """Stack"""
        for _ in range(self.num):
            self.all.append(input())
    def is_empty(self):
        """."""
        if self.num <= 0:
            return True
        else:
            return False
    def pop(self):
        """ลบข้อมูลที่อยู่ส่วน Top ของ Stack"""
        if self.is_empty():
            return "None"
        else:
            last = self.all[-1]
            self.all.pop()
            self.num -= 1
            return last
    def divided(self):
        """แบ่งกลุ่ม"""
        while GROUPS.num != 0:
            for i in range(GROUPS.group):
                if len(self.newlist) <= i:
                    self.newlist.append([])
                if self.is_empty() != True:
                    self.newlist[i].append(GROUPS.pop())
    def printout(self):
        """for printing"""
        for i in range(self.group):
            print("Group %d: " %(i+1), end="")
            for j in self.newlist[i]:
                if j == self.newlist[i][-1]:
                    print(j)
                else:
                    print("%s, " %j, end="")
 
#input
GROUPS = ArrayStack(input(), input())
GROUPS.push()
#print(GROUPS.all)
GROUPS.divided()
#print(GROUPS.newlist)
GROUPS.printout()