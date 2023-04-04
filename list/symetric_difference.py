if __name__ == '__main__':
    # Get the number of students subscribed to the English newspaper
    n = int(input())
    
    # Get the set of roll numbers of students subscribed to the English newspaper
    english_subs = set(map(int, input().split()))
    
    # Get the number of students subscribed to the French newspaper
    m = int(input())
    
    # Get the set of roll numbers of students subscribed to the French newspaper
    french_subs = set(map(int, input().split()))
    
    # Find the symmetric difference of the two sets to get the roll numbers
    # of students subscribed to English or French newspapers but not both
    exclusive_subs = english_subs.symmetric_difference(french_subs)
    
    # Print the total number of students who have subscriptions to the English
    # or the French newspaper but not both.
    print(len(exclusive_subs))
