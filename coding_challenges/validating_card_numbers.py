import re

n = int(input().strip())
for i in range(n):
    s = input().strip()
    # Check if s starts with 4, 5 or 6 and is followed by 15 digits
    if re.match(r'^[456]\d{15}$', s) or re.match(r'^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$', s):
        # Remove any hyphens and check if there are no consecutive repeated digits
        s = s.replace('-', '')
        if not re.search(r'(\d)\1{3,}', s):
            print('Valid')
            continue
    print('Invalid')

