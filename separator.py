class OddEvenSeparator:
    def __init__(self):
        self.chetn = []
        self.nechetn = []

    def add_number(self, num):
        if num % 2 == 0:
            self.chetn.append(num)
        else:
            self.nechetn.append(num)

    def even(self):
        return self.chetn

    def odd(self):
        return self.nechetn


separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))

