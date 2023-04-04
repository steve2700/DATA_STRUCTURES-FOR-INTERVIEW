import re

def validate_uid(uid):
    # Check that the UID is 10 characters long and contains only alphanumeric characters
    if not re.match(r'^[a-zA-Z0-9]{10}$', uid):
        return False
    
    # Check that the UID contains at least 2 uppercase letters, 3 digits, and no repeated characters
    if len(set(uid)) != len(uid):
        return False
    if sum(1 for c in uid if c.isupper()) < 2:
        return False
    if sum(1 for c in uid if c.isdigit()) < 3:
        return False
    
    # If all checks pass, the UID is valid
    return True

# Read the number of test cases from input
t = int(input())

# Process each test case
for i in range(t):
    # Read the UID from input
    uid = input().strip()
    
    # Validate the UID and print the result
    if validate_uid(uid):
        print('Valid')
    else:
        print('Invalid')

