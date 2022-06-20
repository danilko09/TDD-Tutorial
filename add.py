import re

def Add(numbers):
    numbers = split(numbers, ["\n", ","])
    ints = map(int, numbers)
    return sum(ints)

def split(numbers, list_of_delimiters):
    tmp = f"{list_of_delimiters[0]}"
    for delim in list_of_delimiters[1:]:
        tmp += f"|{delim}"
    return re.split(tmp, numbers)
