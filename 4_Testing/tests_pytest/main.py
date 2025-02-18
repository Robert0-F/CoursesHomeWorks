class Calc:
    num = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, x=None, y=None):
        if x is None or y is None:
            return self.x + self.y
        else:
            return x + y


    def average(self, lis):
        summ = 0
        for i in lis:
            summ +=i
        return round(summ/len(lis), 2)


    @staticmethod
    def mult(x, y):
        return x * y

    def __add__(self, other):
        self.num += other
        return self.num