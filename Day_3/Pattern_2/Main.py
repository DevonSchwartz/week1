num = input("How many lines would you like to print?:")
count = int(num) * 2
count_2 = int(num)
while int(count_2) > 0:
    print (('*') * count)
    count -= 2
    count_2 -= 1
