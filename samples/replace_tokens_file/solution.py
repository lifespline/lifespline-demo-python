import fileinput
import sys
import re

# path is relative to the python interpreter or an absolute path
path = "example.md"
pattern_token_1 = 'TOKEN_1'
pattern_token_2 = 'TOKEN_2'

for line in fileinput.input(path, inplace=1):

    if 'TOKEN_1' in line:
        line = line.replace('TOKEN_1', "token 1\nreplaced by\nmultiple lines")
    elif 'TOKEN_2' in line:
        line = line.replace('TOKEN_2', "token 2 replaced by a single line")

    sys.stdout.write(line)
