import re

# path = 'P:\\123\P4E\w3\\regex_sum_42.txt'
path = "P:\\123\\P4E\\w3\\regex_sum_113413.txt"

print (path)
file = open(path)
res = 0
for line in file:
    t = re.findall('[0-9]+', line)
    nums = [int(n) for n in t]
    res += sum(nums)

print (res)

print(chr(108), chr(105), chr(115), chr(116))