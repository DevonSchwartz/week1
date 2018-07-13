num = input("How many rows would you like?:")
peak = 5
count = 1
count_2 = 0
while int(count) < int(num):
    count += 1
    while int(count_2) < int(peak):
        count_2 += 1
        print (('*') * count_2)

    while int(count_2) <= int(peak):
        count_2 -= 1
        print (('*') * count_2)
