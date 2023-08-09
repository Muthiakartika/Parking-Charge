# Created by : Muthia Kartika Putri
# Student ID : E1800189
# Date : 24 March 2021
# Subject Code : BIT 100
# Assignment 1 - Task 1
# Editor : Pycharm
# Python Version : Python 3.9
# This program is created to generate parking fees automatically
# and also to calculate the total cost of parking for a day

# A function with name "parkingCharge" as the main function from this
# program
def parkingCharge():

    timeOutStatus = True # declaring variable timeOutStatus with True value
    timeInStatus = True  # declaring variable timeInStatus with True value
    totalCharges = 0     # declaring variable totalCharges with 0 value
    totalOverallCharges = 0 # declaring variable totalOverallCharges
                            # with 0 value
    totalVehicle = 0     # declaring variable totalCharges with 0 value
    amount = 0           # declaring variable amount with 0 value

    # Displaying the introduction message
    print("~~~~~~~ Welcome to Help Parking Charge ~~~~~~~")
    print("This program will help you to calculate the "
          "amount of your parking payment\n")

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

        hourIn = timeIn // 100  # split the data from variable
                                # timeIn into hourIn

        minuteIn = timeIn % 100 # split the data from variable
                                # timeIn into minuteIn

        hourOut = timeOut // 100 # split the data from variable
                                 # timeOut into hourOut

        minuteOut = timeOut % 100# split the data from variable
                                 # timeOut into minuteOut


        # validate user input
        # if data in minuteIn is less than 60 and data in hourIn is less
        # then 24, timeInStatus data is True
        if (minuteIn < 60 and hourIn < 24):
            timeInStatus = True

        # but if the data in minuteIn is more than 60 and data in hourIn is
        # more than 24, timeInStatus data is False. It will give a
        # notification shown that if time in is not valid
        else:
            print("- Time in is not valid !")
            timeInStatus = False

        # if data in minuteOut is less than 60 and data in hourOut is less
        # then 24, timeOutStatus data is True
        if (minuteOut < 60 and hourOut < 24):
            timeOutStatus = True

        # but if the data in minuteOut is more than 60 and data in
        # hourOut is more than 24, timeOutStatus data is False. It will
        # give a notification shown that if time Out is not valid
        else:
            print("- Time Out is not valid !\n")
            timeInStatus = False

        # if hourOut data is smaller than hourIn, or hourOut data is
        # equal to hourIn and minuteIn data is bigger than minuteOut,
        # timeInStatus and timeOutStatus data is false. and it will give
        # a notification shown that if time out can't be equal to or
        # earlier than time in
        if (hourOut < hourIn or (hourOut == hourIn
                and minuteIn > minuteOut)):
            print("- Time out CANNOT be equal to or earlier than time "
                  "in!\n")
            timeInStatus = False
            timeOutStatus = False

        # calculate the duration
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

        # Calculate the rounded hour
        # if remainMinute data, the result from calculation duration (
        # minute data) is bigger than 0, the remainHour data (result
        # from calculation duration for hour data) will be added by 1
        # and it will be stored in totalHour data
        if (remainMinute > 0):
            totalHour = remainHour + 1

        # But,if the remainMinute less than 0, the totalHour data is the
        # remainHour
        else:
            totalHour = remainHour

        # This is used to distinguish the program if the data
        # entered is correct, so that if the data entered is wrong
        # and displays an error message, proof of the parking charge
        # will not be displayed, as well as the total parking charge data
        # amount that has been carried out during the day.
        if (timeInStatus == True and timeOutStatus == True):

            # calculate the compute charge
            # If the user input c by using lowercase or uppercase letters
            # in the vehicle data, the program will automatically calculate
            # the parking charge for the vehicle with type C
            if(vehicle == 'C' or vehicle == 'c'):

                vehicle = "Car" # Vehicle name will be changed into Car
                                # and it will be stored into variable
                                # vehicle

                # If the parking duration is less than or for 3 hours,
                # the parking charge will be charged a rate of 0.80
                if(totalHour <= 3):
                    amount = 0.80*totalHour

                # but, if the parking duration is more than 3 hours,
                # the following charge parking duration (after 3 hours)
                # will be charged a rate of 1.50
                else:
                    after3Hour = totalHour - 3
                    amount = (after3Hour*1.50)+(3*0.80)

            # If the user input b by using lowercase or uppercase letters
            # in the vehicle data, the program will automatically calculate
            # the parking charge for the vehicle with type b
            elif(vehicle == 'B' or vehicle == 'b'):

                vehicle = "Bus" # Vehicle name will be changed into Bus
                                # and it will be stored into variable
                                # vehicle

                # If the parking duration is less than or for 2 hours,
                # the parking charge will be charged a rate of 1.50
                if(totalHour <= 2):
                    amount = 1.50 * totalHour

                # but, if the parking duration is more than 2 hours,
                # the following charge parking duration (after 2 hours)
                # will be charged a rate of 2.30
                else:
                    after2Hour = totalHour - 2
                    amount = (after2Hour * 2.30)+(2*1.50)

            # If the user input t by using lowercase or uppercase letters
            # in the vehicle data, the program will automatically calculate
            # he parking charge for the vehicle with type t
            elif (vehicle == 'T' or vehicle == 't'):

                vehicle = "Truck" # Vehicle name will be changed into Truck
                                  # and it will be stored into variable
                                  # vehicle

                # If the parking duration is less than or for 1 hours,
                # the parking charge will be charged a rate of 2.00
                if(totalHour <= 1):
                    amount = 2.00 * totalHour

                # but, if the parking duration is more than 1 hours,
                # the following charge parking duration (after 1 hours)
                # will be charged a rate of 3.40
                else:
                    afterAnHour = totalHour - 1
                    amount = (afterAnHour*3.40)+(1*2.00)


            totalTax = amount*(6/100)  # calculate the tax
            totalAmount = amount + totalTax # calulate total amount with
            # tax

            # if vehicle data is not empty, then the number of vehicles
            # that have parked will be counted
            if(vehicle != None):
                totalVehicle += 1

            # calculate the total charges of all vehicles
            # that have been parked during the day
            totalOverallCharges = totalOverallCharges + totalAmount

            # Displaying the total charges and bills
            # It will print "~" as many as 30 pieces. This is the
            # opening line
            print("~" *30)

            # This will print the parking lot name
            print("HELP PARKING LOT CHARGE\n")

            # This will display the name of the vehicle that has parked
            print("Type of vehicle: ", vehicle, "\n")

            # This will display the vehicle exit time,
            # here I use {: 02d}.format()
            # to display the 0 in front of the number
            print("TIME-OUT\t\t {:02d}".format(hourOut),
                  ": {:02d}".format(minuteOut))

            # This will display the vehicle enter time,
            # here I use {: 02d}.format()
            # to display the 0 in front of the number
            print("TIME-IN\t\t\t {:02d}".format(hourIn),
                  ": {:02d}".format(minuteIn))

            # this is the dividing line
            print("\t\t\t\t --------")

            # This will display the vehicle total time,
            # here I use {: 02d}.format() for displaying the 0
            # in front of the number
            print("PARKING TIME\t {:02d}".format(remainHour), ": {:02d}"
                  .format(remainMinute))

            # This will display the total hour that has been rounded
            print("ROUNDED TOTAL\t\t ", totalHour)

            # this is the dividing line
            print("\t\t\t\t --------")

            # This will display the total charge without the tax.
            # Here I use {:.2f).format() for displaying the 0 behind of
            # the number
            print("TOTAL CHARGE\t RM {:.2f}".format(amount))

            # This will display the total tax. Here I use {:.2f).format()
            # for displaying the 0 behind of the number
            print("GST (6%)\t\t RM {:.2f}".format(totalTax))

            # this is the dividing line
            print("\t\t\t\t --------")

            # This will display the total amount with the tax. Here I
            # use {:.2f).format() for displaying the 0 behind of the
            # number
            print("TOTAL:\t\t\t RM {:.2f}".format(totalAmount))

            # It will print "~" as many as 30 pieces. This is the
            # closing line
            print("~" *30)

        # Inputing vehicle type and storing the data into variable
        # vehicle. I repeat it again to input the vehicle type
        vehicle = input("Vehicle type <C>ar, <B>us, <T>ruck "
                        "(<Enter> to quit):")

    # If the number of parked vehicles is empty, a notification will
    # appear that the parking lot is closed for today
    if(totalVehicle == None):
        print("Parking Lot is closed for today....")

    # otherwise, it will display the total overall charges from vehicles
    # that have parked during the day
    else:
        print("Total collection for the day: RM"
              " {:.2f}".format(totalOverallCharges))

# This is calling the parkingCharge function
parkingCharge()
