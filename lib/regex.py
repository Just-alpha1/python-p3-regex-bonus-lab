import re

my_pattern = r"^\s*(.*(?:today|day).*?[.?])\s*$"
my_regex = re.compile(my_pattern, re.MULTILINE)

