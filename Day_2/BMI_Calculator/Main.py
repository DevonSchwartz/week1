def response(BMI):
    if BMI < float(18.5): #if BMI is less than 18.5(any unit)
        print ("You are underweight") # print "You are underweight"
    if BMI > float(18.5) and BMI < float(25): # if the BMI is greater than 18.5, but less than 25
        print ("Normal Weight")# print "Normal Weight"
    elif BMI > float(25) and BMI < float(30):# if the BMI is greater than 25 but less than 30
        print ("Over Weight")# print "Over Weight"
    elif BMI > float(30) and BMI < float(40):# if the BMI is greater than 30 but less than 40
        print ("You are obese") # print "You are obese"
    elif BMI > float(40): # If the BMI is greater than 40
        print ("You are morbidly obese. Call a Doctor!") #print "You are morbidly obsese, call a doctor"


def Customary():

    Weight = eval(input("Weight(lb):"))
    # Asks for the input of someone's weight in pounds, and stores that value in "weight" variable

    Height = eval(input("Height(in):"))
    # Asks for the input of someone's height in inches, and stores that value in "Height" variable

    BMI = (703 * (Weight/Height**2)) #Inputs variables into BMI formula

    response(BMI) #Applies corresponding responses to calcualted BMI

    print (str(int(BMI))) #print the BMI as a string and integer

def Metric():
    Weight = eval(input("Weight(kilograms):")) # Asks for the input of someone's weight in kilograms, and stores that value in "weight" variable
    print ("Press 'C' to enter your height in centimeters. Press 'M' to enter your height in meters")
    Options = input("Choice:")
    if Options == "M":
        Height = eval(input("Height(meters):")) # Asks for the input of someone's height in meters, and stores that value in "Height" variable
    elif Options == "C":
        Height = eval(input("Height(centimeters):"))
        Height = int(Height) / 10

    BMI = ( (Weight) / (Height ** 2)) #Inputs variables into BMI formula

    response(BMI) # Applies corresponding response to calculated  BMI

    print (str(int(BMI))) # print BMI as a string and integer


Unit = input("Customary or Metric?:")
    # the input of "Customary" or Metric is stored into the variable "Unit"

if Unit == "Customary" or Unit == "customary": # if the input of "Unit" is "Customary", call the customary function
    Customary()

elif Unit == "Metric" or Unit == "metric": # if the input of "Unit" is metric, call the metric function
    Metric()
