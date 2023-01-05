# s = input()

# s = '|'.join([f'"{word}"' for word in s.split() if len(word) == 1])

# print(s)

# s = input()

# s = [word + ' { printf("%s - reserved word\\n", yytext); return ' + word.strip('"').upper() + '; }' for word in s.split("|")]

# for x in s:
#     print(x)

# for x in s:
#     print("%token " + x.strip('"').upper()[:x[1:].find('"')])

import re

def upper_repl(match):
    return match.group(1).upper()

with open('productions.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('::=', ':').replace('\n', '')
        line = re.sub(r'"([^"]*)"', upper_repl, line)
        # line = re.sub(r'"([^)"]*"', r'\1', line)
        print(line)
