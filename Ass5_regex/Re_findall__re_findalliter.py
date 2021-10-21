# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'
memory = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', input(), flags=re.I)

if memory:
    for i in memory:
        print(i)
else:
    print(-1)
