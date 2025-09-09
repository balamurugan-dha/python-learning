class Person:
    def __init__(self, name):
        self.name = name

    def invite(self):
        print('Welcome', self.name)
    
p1 = Person("Balamurugan")

p1.invite()