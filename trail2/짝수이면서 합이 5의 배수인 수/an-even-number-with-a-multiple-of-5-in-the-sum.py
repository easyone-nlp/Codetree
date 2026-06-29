n = int(input())

def magic_number(n):
    number_sum = int(n % 10) + int((n - (n % 10)) // 10)
    # print(number_sum)
    if n % 2 == 0 and number_sum % 5 == 0:
        return "Yes"
    else:
        return "No"

answer = magic_number(n)
print(answer)