def addition(x,y):
    total = float(x) + float(y) # Store sum of x and y in "total"
    return (str(total)) # Return the amount of total

def subtraction(x,y):
    total = float(x) - float(y) # Store sum of x and y in "total"
    return (str(total)) # Return the amount of total

def multiplication(x,y):
    i = 0 # total
    ii = 0 # Counter
    while int(ii) < int(y): # Loops ii until it is equal to y ( the amount of groups x is being put into)
        i += int(x) # i = x(input) + i(0). It counts the amount of times the loop is run
        ii += 1 # ii = ii(0) + 1 ; ii = 1 (ii will be the total returned)
        #if ii == y: # if ( and when) the value of i is equal to y
    return (str(float(i))) # return i (the total)

# def mudulo(x,y):
#     i = 0
#     ii = 0
#
# def division(x,y):
#     i = 0 # total
#     ii = 0 # Counter
#     while int(ii) < int(y): # Loop ii until it equals y
#         ii += 1 # i equals y plus the value of y (which changes every time the loop runs)
#         i = multiplication(ii,int(y)) # Counts the amount of times the loop is run
#     return (str(i)) # Prints the amount of times the loop is run (principle of division. How many groups x is in y)
#
# def base2_to_base10(base_2):
#     base_2 = str(base_2) # input as a string
#     base_2_len = len(base_2)  # A counter
#     ii = 0 # Counter
#     for i in range(len(base_2)): # for i(each digit) in however many digits base_2(binary number) is
#         base_2[i] # Iterate
#         if str(i) == 1: # If i (digit) equals 1
#             ii +=  str(base_2[i]) * (2 ** i) # ii(counter) equals ii plus i * 2 to the power of the length of base_2(number of digits)
#             base_2_len -= 1
#         elif str(i) == 0:
#             base_2_len-=1
#     return (str(i))
#
# def base2_to_base8 (base_2):
#     [num_bef_dec, num_after_dec] = base_2.split(".")
#     output = ""
#     count = 0
#     side_a = len(num_bef_dec)
#     side_b = len(num_after_dec)
#
#     if side_a % 3 == 1:
#         num_bef_dec = num_bef_dec + "0"
#     if side_a % 3 == 2:
#         num_bef_dec = num_bef_dec + "00"
#     if side_b % 3 == 1:
#        num_after_dec = num_after_dec.append("0")
#     if side_b % 3 == 2:
#        num_after_dec = num_bef_dec.append("00")
#
#     for index in range(0, len(num_bef_dec), 3):
#         cur_group = num_bef_dec[index:index+3]
#
#         if cur_group == "000":
#             output = output + "0"
#         elif cur_group == "001":
#             output = output + "1"
#         elif cur_group == "010":
#             output = output + "2"
#         elif cur_group == "011":
#             output = output + "3"
#         elif cur_group == "100":
#             output = output + "4"
#         elif cur_group == "101":
#             output = output + "5"
#         elif cur_group == "110":
#             output = output + "6"
#         elif cur_group == "111":
#             output = output + "7"
#         print (str(output))
#     for index in range(0,len(num_after_dec), 3):
#          cur_group = num_after_dec[index: index + 3]
#
#          if cur_group == "000":
#             output = output + "0"
#          elif cur_group == "001":
#             output == output + "1"
#          elif cur_group == "010":
#             output = output+ "2"
#          elif cur_group == "011":
#             output = output + "3"
#          elif cur_group == "100":
#             output = output + "4"
#          elif cur_group == "101":
#             output = output + "5"
#          elif cur_group == "110":
#             output = output + "6"
#          elif cur_group == "111":
#             output = output + "7"
#     print (str(output))





def Choice():
    Question = input("What do you want to do\
    Multiplication, Division, Subtraction, Addition, Convert Binary to Base10, Base_8?")
    if Question == "addition" or Question == "Addition":
        var1 = input("First Number:")
        var2 = input("Second Number:")
        print (addition(var1,var2))
    elif Question == "subtraction" or Question == "Subtraction":
        var1 = input("First Number:")
        var2 = input("Second Number:")
        print (subtraction(var1,var2))
    elif Question == "Multiplication" or Question == "multiplication":
        var1 = input("First Number:")
        var2 = input("Second Number:")
        print (multiplication(var1,var2))
#     elif Question == "Division" or Question == "division":
#         var1 = input("First Number:")
#         var2 = input("Second Number:")
#         print (division(var1,var2))
#     elif Question == "C":
#         binary_number = input("Binary Number:")
#         print (base2_to_base10(binary_number))
#     elif Question == "Base_8":
#         binary_number = input("Binary Number:")
#         base2_to_base8(binary_number)
Choice()
