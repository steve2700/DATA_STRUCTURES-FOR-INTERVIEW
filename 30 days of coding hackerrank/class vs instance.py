class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        #we checking if age < 0 to return the error age is not valid
        
        if (initialAge < 0):
            print('Age is not valid, setting age to 0.')
            self.age = 0
        else:
            self.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        #the code speaks for itself!
        #if age is less than 13 print you are young
        #if age greater or equal to 13 and less than 18 print you are a teenager
        if self.age < 13:
            print('You are young.')
        elif self.age >=13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
        

t = int(input())
