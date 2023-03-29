class TheAge:
    def setAge(self, num):
        self.age = num

    def getAge(self):
        return self.age
    
mbali= TheAge()
mbali.setAge(6)
print(mbali.getAge())

Stewart = TheAge()
Stewart.setAge(20)
print(Stewart.getAge())
