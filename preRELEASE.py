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
    print("time: Avaliable: Sold: MoneyTaken:")
    print("trains up")
    print(train1[0], train1[1]*seatsPerCoach, train1[2], train1[3])
    print(train2[0], train2[1]*seatsPerCoach, train2[2], train2[3])
    print(train3[0], train3[1]*seatsPerCoach, train3[2], train3[3])
    print(train4[0], train4[1]*seatsPerCoach, train4[2], train4[3])
    print("trains down")
    print(train1B[0], train1B[1]*seatsPerCoach, train1B[2], train1B[3])
    print(train2B[0], train2B[1]*seatsPerCoach, train2B[2], train2B[3])
    print(train3B[0], train3B[1]*seatsPerCoach, train3B[2], train3B[3])
    print(train4B[0], train4B[1]*seatsPerCoach, train4B[2], train4B[3])

while True:
    displayBoard()
    print("welcome to the ticket booking system:")
    groupSize = int(input("please enter the number of people you would like to book:"))
    timeTrainUp = int(input("time of train up:"))
    timeTrainDown = int(input("time of train down:"))
    if timeTrainDown >= timeTrainUp:
        print("please select a train down after the train up")
        input
    
    