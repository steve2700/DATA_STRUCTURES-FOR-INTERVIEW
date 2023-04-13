# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

phone_book = {}

for i in range(n):
    entry = input().split()
    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone
    
while True:
    try:
        query = input()
        if query in phone_book:
            phone = phone_book[query]
            print(query + "=" + phone)
        else:
            print("Not found")
    except:
        break


