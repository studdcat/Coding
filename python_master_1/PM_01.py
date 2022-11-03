num = input("input number ")

if num.isdigit():
    result = ""
    num = num[::-1]
    for i, x in enumerate(num):
        i += 1
        if len(num) != i and i % 3 == 0:
           result += x + ","
        else:
            result += x
    result = result[::-1]
    print(result)
else:
    print("not number")