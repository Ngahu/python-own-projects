class Hero:
    def _init_(self,name):
        self.name = name
        self.health = 100
    def eat(self,food):
        if (food == 'apple'):
            self.health -=100
        elif (food == 'pizza'):
            self.health +=20

print Bob.name
print Bob.health
Bob.eat('apple')
print Bob.health