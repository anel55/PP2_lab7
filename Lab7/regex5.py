import re

def starts_a_ends_b(text):
    patterns = '^a.*?b$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')
    