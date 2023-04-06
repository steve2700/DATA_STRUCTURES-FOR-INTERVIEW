#lets code good luck!
#Declare 3 variables: one of type int, one of type double, and one of type String.
#Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
#Use + the  operator to perform the following operations:
#Print the sum i of  plus your int variable on a new line.
#Print the sum  d of  plus your double variable to a scale of one decimal place on a new line.
#Concatenate s with the string you read as input and print the result on a new line.
#The first line contains an integer that you must sum with i.
#The second line contains a double that you must sum with d.
#The third line contains a string that you must concatenate with s.

# reading 3 variable int , float and string
i = 4
d = 4.0
s = 'Hackerrank'

# declare 3 variables and read them 
i2 = int(input())
d2 = float(input())
s2 = input()

#print the sum of i of int
print(i + i2)
#print the sum of the double to sum with d 
# and round off to 1 decimal place
print(round(d + d2, 1))
#print the string that concatenate with s
print(s + s2)









