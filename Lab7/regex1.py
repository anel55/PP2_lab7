import re
def text_match(content):
        patterns = '^a(b*)$'
        if re.search(patterns,  content):
                return 'Found a match!'
        else:
                return('Not matched!')


