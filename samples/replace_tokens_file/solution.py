import fileinput
import sys
import re

# path is relative to the python interpreter or an absolute path
path = "example.md"
pattern_token_1 = 'TOKEN_1'
pattern_token_2 = 'TOKEN_2'
pattern_token_3 = 'TOKEN_3\nTOKEN_4'

# replacing single line token
for line in fileinput.input(path, inplace=1):

    if 'TOKEN_1' in line:
        line = line.replace('TOKEN_1', "token 1\nreplaced by\nmultiple lines")
    elif 'TOKEN_2' in line:
        line = line.replace('TOKEN_2', "token 2 replaced by a single line")

    sys.stdout.write(line)

# replacing multiple line token
file = open(path, 'r')
data = ''
for line in file:
    data += line
data.replace(pattern_token_1, "token 1\nreplaced by\nmultiple lines")
data.replace(pattern_token_2, "token 2 replaced by a single line")
data = data.replace(pattern_token_3, "token 3 replaced by a single line")
file.close()

file = open(path, 'w')
file.write(data)
file.close()

# token 1
# replaced by
# multiple lines
# token 2 replaced by a single line
# token 3 replaced by a single line