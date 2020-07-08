class partyanimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)


s = partyanimal('sally')
s.party()
j = partyanimal('jim')
j.party()
s.party()


class footballfan(partyanimal):
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, 'points', self.points)


p = footballfan('cat')
p.party()
p.touchdown()
