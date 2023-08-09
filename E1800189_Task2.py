# Created by : Muthia Kartika Putri
# Student ID : E1800189
# Subject Code : BIT 100
# Date : 24 March 2021
# Assignment 1 - Task 2
# Editor : Pycharm
# Python Version : Python 3.9
# This program is created to generate parking fees automatically
# and also to calculate the total cost of parking for a day

# A function with name "parkingCharge" as the main function from this
# program
def parkingCharge():

    global totalAmount      # A global variable to declare totalAmount
    totalOverallCharges = 0 # Declaring variable totalOverallCharge with
                            # 0 value
    totalVehicle = 0        # Decalring variable totalVehicle with 0 value

    # Calling displayIntroductionMessage function
    displayIntroductionMessage()

    # Inputting vehicle type and storing the data into variable vehicle
    vehicle = input("Vehicle type <C>ar, <B>us, <T>ruck (<Enter> to "
                    "quit):")

    # looping if vehicle data is not empty. Here I use sentinel while
    # loop for looping my program
    while vehicle != "":

        # inputting time in data and storing the data into
        # variable timeIn
        timeIn = int(input("Time in (24-hour mode, e.g. 0900):"))

        # inputting time out data and storing the data into
        # variable timeOut
        timeOut = int(input("Time out (24-hour mode, e.g. 1130):"))

        # Calling split function, to split between the hour and minute
        # from variable timeIn. And it will be stored into variable hourIn
        # and minuteIn
        hourIn, minuteIn = split(timeIn)

        # Calling split function, to split between the hour and minute
        # from variable timeOut. And it will be stored into variable
        # hourOut and minuteOut
        hourOut, minuteOut = split(timeOut)

        # Calling validateEntry function, and it will be stored into
        # valid variable
        valid = validateEntry(timeIn, timeOut)

        # Print the valid variable to shown the notification of validation
        print(valid)

        # If valid variable doesn't contain any data, than the program
        # will compile this code
        if (valid == ""):

            # Calling computeCharge function, and stored the data into
            # variable charge
            charge = computeCharge(vehicle, timeIn, timeOut)

            gst = charge * (6 / 100)   # Calculate the tax
            totalAmount = charge + gst # calulate total amount with tax

            # calculate the total charges of all vehicles
            # that have been parked during the day
            totalOverallCharges = totalOverallCharges + totalAmount

            # if vehicle data is not empty, then the number of vehicles
            # that have parked will be counted
            if (vehicle != None):
                totalVehicle += 1

            # Calling displayBill function. This function will print
            # the total charges and bills
            displayBill(vehicle, timeIn, timeOut, charge, gst)

        # Inputting vehicle type and storing the data into variable vehicle
        vehicle = input("Vehicle type <C>ar, <B>us, <T>ruck (<Enter> to "
                        "quit):")

    # If the number of parked vehicles is empty, a notification will
    # appear that the parking lot is closed for today
    if (totalVehicle == None):
        print("Parking Lot is closed for today....")

    # Otherwise, it will display the total overall charges from vehicles
    # that have parked during the day
    else:
        print("Total collection for the day: RM {:.2f}"
              "".format(totalOverallCharges))

# This function is created for displaying an introduction message
# This function doesn't have a parameter. Also it doesn't need a return
# data
def displayIntroductionMessage():

    # It will print the introduction message
    print("~~~~~~~ Welcome to Help Parking Charge ~~~~~~~")
    print("This program will help you to calculate the "
          "amount of your parking payment\n")


# This function is created for splitting the time between the hour and
# minute. This function have a parameter
def split(aTime):

    hour = aTime // 100 # split the data from variable
                        # aTime into hour
    minute = aTime % 100# split the data from variable
                        # aTime into minute

    # It will return an integer data from hour and minute variables
    return hour, minute

# This function is created for sorting the vehicle type
# based on user input. This function have a parameter
def vehicleString(vType):

    vehicle = "" # Declaring vehicle variable

    # If the user input c by using lowercase or uppercase letters
    # in the vehicle data,vehicle name will be changed into Car
    # and it will be stored into variable
    # vehicle
    if (vType == "c" and vType == "C"):
        vehicle = "Car"

    # But, if the user input b by using lowercase or uppercase letters
    # in the vehicle data,vehicle name will be changed into Bus
    # and it will be stored into variable
    # vehicle
    elif (vType == "b" and vType == "B"):
        vehicle = "Bus"

    # Otherwise, if the user input c by using lowercase or uppercase
    # letters in the vehicle data,vehicle name will be changed into Truck
    # and it will be stored into variable vehicle
    elif (vType == "t" and vType == "T"):
        vehicle = "Truck"

    return vehicle # It will return a string data from vehicle variable

# This function is created for calculating the rounded hour. This
# function have 2 parameter
def roundedHour(hour, minute):

    # if remainMinute data, the result from calculation duration (
    # minute data) is bigger than 0, the remainHour data (result
    # from calculation duration for hour data) will be added by 1
    # and it will be stored in totalHour data
    if (minute > 0):
        totalHour = hour + 1

    # But,if the remainMinute less than 0, the totalHour data is the
    # remainHour
    else:
        totalHour = hour

    return totalHour # It will return the totalHour variable

# This function is created for validating the user input. This function
# have 2 parameter
def validateEntry(timeIn, timeOut):

    valid = "" # Declaring valid variable

    # Calling split function, to split between the hour and minute
    # from variable timeIn. And it will be stored into variable hourIn
    # and minuteIn
    hourIn, minuteIn = split(timeIn)

    # Calling split function, to split between the hour and minute
    # from variable timeOut. And it will be stored into variable hourOut
    # and minuteOut
    hourOut, minuteOut = split(timeOut)

    # If data in minuteIn is less than 60 and data in hourIn is less
    # then 24, than the variable valid is empty
    if (minuteIn < 60 and hourIn < 24):
        valid += ""

    # But if the data in minuteIn is more than 60 and data in hourIn is
    # more than 24, than the variable valid is not empty. It will stored a
    # notification shown that if time in is not valid
    else:
        valid += "- Time in is not valid !\n"

    # If data in minuteOut is less than 60 and data in hourOut is less
    # then 24, than the variable valid is empty
    if (minuteOut < 60 and hourOut < 24):
        valid += ""

    # But if the data in minuteOut is more than 60 and data in hourOut is
    # more than 24, than the variable valid is not empty. It will stored a
    # notification shown that if time out is not valid
    else:
        valid += "- Time Out is not valid !\n"

    # Otherwise, if hourOut data is smaller than hourIn, or hourOut data is
    # equal to hourIn and minuteIn data is bigger than minuteOut,
    # the variable valid is not empty. It will stored a notification
    # shown that if time out can't be equal to or
    # earlier than time in
    if (hourOut < hourIn or (hourOut == hourIn and minuteIn > minuteOut)):
        valid += "- Time out CANNOT be equal to or earlier than time in!\n"

    return valid # It will return a string data from valid variable

# This function is created for calculating the duration. This function
# have 2 parameter
def computeDuration(timeIn, timeOut):

    # Calling split function, to split between the hour and minute
    # from variable timeIn. And it will be stored into variable hourIn
    # and minuteIn
    hourIn, minuteIn = split(timeIn)

    # Calling split function, to split between the hour and minute
    # from variable timeOut. And it will be stored into variable hourOut
    # and minuteOut
    hourOut, minuteOut = split(timeOut)

    # if minuteOut data is bigger than minuteIn data, the hourOut
    # data will be reduced by hourIn data, so does the minuteOut. It
    # will be reduced by minuteIn
    if (minuteOut > minuteIn):
        remainHour = hourOut - hourIn
        remainMinute = minuteOut - minuteIn

    # Otherwise, if minuteIn data is bigger than minuteOut,
    # the hourOut data will be reduced by 1 and after that it will
    # be reduced by hourIn. But minuteOut data will be added by 60
    # and after that it will be reduced by minuteIn
    elif (minuteIn > minuteOut):
        remainHour = (hourOut - 1) - hourIn
        remainMinute = (minuteOut + 60) - minuteIn

    return remainHour, remainMinute # It will return 2 integer value
                                    # from remainHour and remainMinute
                                    # variables


# This function is created for computing the charge from this parking
# lot. This function have 3 parameter.
def computeCharge(vType, timeIn, timeOut):

    amount = 0 # Declaring amount variable

    # Calling computeDuration function and storing the data into
    # totalHour and totalMinute variables
    totalHour, totalMinute = computeDuration(timeIn, timeOut)

    # Calling the roundedHour function and storing the data into
    # totalHour_round variable
    totalHour_round = roundedHour(totalHour, totalMinute)

    # If the user input c by using lowercase or uppercase letters
    # in the vehicle data, the program will automatically calculate
    # the parking charge for the vehicle with type C
    if (vType == 'C' or vType == 'c'):

        # If the parking duration is less than or for 3 hours,
        # the parking charge will be charged a rate of 0.80
        if (totalHour_round <= 3):
            amount = 0.80 * totalHour_round

        # but, if the parking duration is more than 3 hours,
        # the following charge parking duration (after 3 hours)
        # will be charged a rate of 1.50
        else:
            after3Hour = totalHour_round - 3
            amount = (after3Hour * 1.50) + (3*0.80)

    # If the user input b by using lowercase or uppercase letters
    # in the vehicle data, the program will automatically calculate
    # the parking charge for the vehicle with type b
    elif (vType == 'B' or vType == 'b'):

        # If the parking duration is less than or for 2 hours,
        # the parking charge will be charged a rate of 1.50
        if (totalHour_round <= 2):
            amount = 1.50 * totalHour_round

        # but, if the parking duration is more than 2 hours,
        # the following charge parking duration (after 2 hours)
        # will be charged a rate of 2.30
        else:
            after2Hour = totalHour_round - 2
            amount = (after2Hour * 2.30) + (2*1.50)

    # If the user input t by using lowercase or uppercase letters
    # in the vehicle data, the program will automatically calculate
    # he parking charge for the vehicle with type t
    elif (vType == 'T' or vType == 't'):

        # If the parking duration is less than or for 1 hours,
        # the parking charge will be charged a rate of 2.00
        if (totalHour_round <= 1):
            amount = 2.00 * totalHour_round

        # but, if the parking duration is more than 1 hours,
        # the following charge parking duration (after 1 hours)
        # will be charged a rate of 3.40
        else:
            afterAnHour = totalHour_round - 1
            amount = (afterAnHour * 3.40) + (1*2.00)

    return amount # It will return an integer data from amount variable

# This function is created for displaying a bill from parking charge.
# This function have 5 parameter
def displayBill(vType, timeIn, timeOut, charge, gst):

    # Displaying the total charges and bills
    # It will print "~" as many as 30 pieces. This is the
    # opening line
    print("~" * 30)

    # This will print the parking lot name
    print("HELP PARKING LOT CHARGE\n")

    # This will display the name of the vehicle that has parked. Here I
    # call vehicleString function for displaying the vehicle name thas
    # has parked
    print("Type of vehicle: ", vehicleString(vType), "\n")

    # This will display the vehicle exit time, here I use {: 02d}.format()
    # to display the 0 in front of the number. Here I call split
    # function for displaying the exit time
    print("TIME-OUT\t\t {:02d}".format(split(timeOut)[0]),
          ": {:02d}".format(split(timeOut)[1]))

    # This will display the vehicle enter time, here I use {: 02d}.format()
    # to display the 0 in front of the number. Here I call split
    # function for displaying the enter time
    print("TIME-IN\t\t\t {:02d}".format(split(timeIn)[0]),
          ": {:02d}".format(split(timeIn)[1]))

    # this is the dividing line
    print("\t\t\t\t --------")

    # This will display the vehicle total time, here I use {:
    # 02d}.format() for displaying the 0 in front of the number. Here I
    # call computeDuration function for displaying the duration of
    # parking time
    print("PARKING TIME\t {:02d}".format(computeDuration(timeIn,
        timeOut)[0]), ": {:02d}".format(computeDuration(timeIn,
        timeOut)[1]))

    # This will display the total hour that has been rounded. Here I
    # call roundedHour function for displaying the rounded hour from the
    # parking charge
    print("ROUNDED TOTAL\t\t ", roundedHour(computeDuration(timeIn,
        timeOut)[0], computeDuration(timeIn, timeOut)[1]))

    # this is the dividing line
    print("\t\t\t\t --------")

    # This will display the total charge without the tax.
    # Here I use {:.2f).format() for displaying the 0 behind of
    # the number
    print("TOTAL CHARGE\t RM {:.2f}".format(charge))

    # This will display the total tax. Here I use {:.2f).format()
    # for displaying the 0 behind of the number
    print("GST (6%)\t\t RM {:.2f}".format(gst))

    # this is the dividing line
    print("\t\t\t\t --------")

    # This will display the total amount with the tax. Here I
    # use {:.2f).format() for displaying the 0 behind of the
    # number
    print("TOTAL:\t\t\t RM {:.2f}".format(totalAmount))

    # It will print "~" as many as 30 pieces. This is the
    # closing line
    print("~" * 30)

parkingCharge() # This is calling the parkingCharge function