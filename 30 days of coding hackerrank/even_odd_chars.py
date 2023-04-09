# Enter your code here. Read input from STDIN. Print output to STDOUT
#practice makes perfect
n = int(input())

for i in range(n):
    s = input()
    even_chars = ""
    odd_chars = ""
    for j in range(len(s)):
        #here we are checking if its even or odd then we iterate 
        if j % 2 == 0:
            even_chars += s[j]
        else:
            odd_chars += s[j]
    print(even_chars + " " + odd_chars)    
