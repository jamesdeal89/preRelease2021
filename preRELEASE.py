# pre-release 2021 CAIE

# TASK 1
# set up screen for the start of the day
# screen shows: train times, number of avaliable tickets left,
# four up, four down
# total eight trips

# one array for each time
seatsPerCoach = 80
price = 25
# time, no. of coaches, tickets bought, total money
train1 = [900, 6, 0, 0]
train2 = [1100, 6, 0, 0]
train3 = [1300, 6, 0, 0]
train4 = [1500, 6, 0, 0]
train1B = [1000, 6, 0, 0]
train2B = [1200, 6, 0, 0]
train3B = [1400, 6, 0, 0]
train4B = [1600, 8, 0, 0]

def displayBoard():
    print("train information")
    print("code: time: Avaliable: Sold: MoneyTaken:")
    print("trains up")
    print("A",train1[0], train1[1]*seatsPerCoach, train1[2], train1[3])
    print("B",train2[0], train2[1]*seatsPerCoach, train2[2], train2[3])
    print("C",train3[0], train3[1]*seatsPerCoach, train3[2], train3[3])
    print("D",train4[0], train4[1]*seatsPerCoach, train4[2], train4[3])
    print("trains down")
    print("AB",train1B[0], train1B[1]*seatsPerCoach, train1B[2], train1B[3])
    print("BB",train2B[0], train2B[1]*seatsPerCoach, train2B[2], train2B[3])
    print("CC",train3B[0], train3B[1]*seatsPerCoach, train3B[2], train3B[3])
    print("DD",train4B[0], train4B[1]*seatsPerCoach, train4B[2], train4B[3])

def checkTiming():
    input()

def bookingDown():
    displayBoard()
    trainDown = input("chose train code down:")
    if trainDown == "AB":
        chosenTimeDown = train1B[0]
        checkTiming()
    elif trainDown == "BB":
        chosenTimeDown = train2B[0]
        checkTiming()
    elif trainDown == "CB":
        chosenTimeDown = train3B[0]
        checkTiming()
    elif trainDown == "DB":
        chosenTimeDown = train4B[0]
        checkTiming()

while True:
    displayBoard()
    print("welcome to the ticket booking system:")
    trainUp = input("chose train code:")
    if trainUp == "A":
        chosenTime = train1[0]
        bookingDown()
    elif trainUp == "B":
        chosenTime = train2[0]
        bookingDown()
    elif trainUp == "C":
        chosenTime = train3[0]
        bookingDown()
    elif trainUp == "D":
        chosenTime = train4[0]
        bookingDown()
    else:
        print("please select only the code of the UP train and in CAPITALS")
        input()

    