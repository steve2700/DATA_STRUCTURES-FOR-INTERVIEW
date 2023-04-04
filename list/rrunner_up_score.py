if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # remove duplicates  using the set () first and we do it descending to find the second number
    arr = sorted(list(set(arr)),reverse = True)
    print(arr[1])