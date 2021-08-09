import re
s = input().strip()
s = s.lower()
s = re.sub('[^a-z0-9]', '', s)
print(s == s[::-1])

# target = ''
# for i in s:
#     if i.isalnum(): target += i
# print(target == target[::-1])