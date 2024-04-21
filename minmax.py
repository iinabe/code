class MinMaxWordFinder:
    def __init__(self):
        self.sent = []

    def add_sentence(self, add):
        for i in add.split():
            self.sent.append((len(i), i))

    def shortest_words(self):
        short = []
        min_ = self.sent[0][0]
        for i in self.sent:
            if i[0] < min_:
                short = [i[1]]
                min_ = i[0]
            elif i[0] == min_:
                short.append(i[1])
        return sorted(short)

    def longest_words(self):
        long = []
        max_ = self.sent[0][0]
        for i in self.sent:
            if i[0] > max_:
                long = [i[1]]
                max_ = i[0]
            elif i[0] == max_:
                if i[1] not in long:
                    long.append(i[1])
        return long

