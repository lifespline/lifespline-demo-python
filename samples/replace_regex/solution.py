import re
s = "abaca"
replaced = re.sub('[bc]', '*', s)
print(replaced)
