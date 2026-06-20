str = input()
str_list = ["apple", "banana", "grape", "blueberry", "orange"]

total = 0

for s in str_list:
    if str in s[2] or str in s[3]:
        total += 1
        print(s)
print(total)