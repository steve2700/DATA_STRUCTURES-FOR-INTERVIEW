#in dictionary we dont have duplicates 
#so lets use this cool feature dict.fromkey()
# to remove duplicates

#cool 
x = ['a', 'b', 'c', 'a' , 'b', 'c', 'd', 'e']
x = list(dict.fromkeys(x))
print(x)