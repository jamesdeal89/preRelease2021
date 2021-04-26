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
    print(train1[0], train1[1]*seatsPerCoach, train1[2])
    print(train2[0], train2[1]*seatsPerCoach, train2[2])
    print(train3[0], train3[1]*seatsPerCoach, train3[2])
    print(train4[0], train4[1]*seatsPerCoach, train4[2])
    


    