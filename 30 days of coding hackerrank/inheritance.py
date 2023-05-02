class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    #however we did not put the score because its not not inheiting on the person class 
    def __init__ (self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #   this is funny!
    # Write your function here
    def calculate(self):
        average_score = sum(self.scores) / len(self.scores)
        if 90 <= average_score <= 100:
            return 'O'
        elif 80 <= average_score <= 90:
            return 'E'
        elif 70 <= average_score <= 80:
            return 'A'
        elif 55 <= average_score <= 70:
            return 'P'
        elif 40 <= average_score <= 55:
            return 'D'
        else:
            return 'T'

line = input().split()
