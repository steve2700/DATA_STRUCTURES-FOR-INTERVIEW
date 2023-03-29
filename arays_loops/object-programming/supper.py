import random
class Animal:
    """lazy programmers"""

    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Black shepperd','pitbull' ,'english'])

    def fetch(self, thing):
        print('%s take the ball!%s'%  (self.name, thing))
d = Dog('dog name:')
print(d.breed)
d.fetch(' ''pitbull')

