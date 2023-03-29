class Sumlist:
    def __init__(self,my_list):
        self.my_list = my_list

    def __add__(self, other):
        new_list = [x + y for x, y in zip(self.my_list, other.my_list)]
        return Sumlist(new_list)
    def __repr__(self):
        return str(self.my_list)
    '''Python is funny'''

a = Sumlist([2, 45, 67, 89, 45])
b = Sumlist([4, 56, 78, 89, 90])
c = a + b    
print(c)


       