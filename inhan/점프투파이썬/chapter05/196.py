class fourcal():
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.first

    def div(self):
        return self.first / self.second


a = fourcal()
b = fourcal()
a.setdata(4, 2)
b.setdata(3, 7)
