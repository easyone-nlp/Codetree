str = input()

new_str = str[0] + str[1:len(str)-2].replace(str[1], 'a',1)+str[-2].replace(str[-2], 'a',1) + str[len(str)-1]
print(new_str)
# print(str)