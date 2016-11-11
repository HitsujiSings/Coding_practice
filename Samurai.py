import random
resultSUM=0

for i in range(100):
    a=[0]*365
    ballcount=0
    fullroom=0   
    #throw ball into 365 room randomly and check the total ball number when     all room have ball.
    while fullroom < 183:
        randomX=random.randint(0,364) #generate 0<=int<=364
        if a[randomX] == 0:
            a[randomX] += 1
            fullroom += 1
            ballcount += 1
    #        print("fullroom=", fullroom, end=" ")
            continue
        ballcount += 1
    resultSUM += ballcount
print(resultSUM/100)
