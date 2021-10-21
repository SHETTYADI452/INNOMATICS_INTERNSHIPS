# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
string=input()
sub_string=input()
m = re.finditer(r'(?=(' + sub_string + '))',string)
anymatch = False
for match in m:
    anymatch = True
    print((match.start(1), match.end(1) - 1))

if anymatch == False:
    print((-1, -1))