import re
text = "WhatANiceDay"
print(re.findall('[A-Z][^A-Z]*', text))