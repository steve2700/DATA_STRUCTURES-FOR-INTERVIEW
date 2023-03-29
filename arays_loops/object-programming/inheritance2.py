class Animal:
    
    """THE ANIMAL"""
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print('%s is hungry eating %s!' %(self.name, food ))

class Dog(Animal):
    """The body of the Dog"""
    def fetch(self, thing):
        print('%s goes after %s' %(self.name, thing))
class cat(Animal):
    """the body of the cat"""
    def cry(self, alone):
        print('%s is feeling bored %s'%(self.name,alone))        
y = Dog('Rangers')
p = cat('mEow')
p.eat('his legs so crazy):')
y.eat('BONES')
y.fetch('ball')
p.cry('no food')






