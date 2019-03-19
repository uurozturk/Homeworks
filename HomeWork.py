from math import *
#convert the number of coordinates to int
numberOfInputs = int(input("How many coodinates do you want to enter: "))
inputs = []
#take coordinates until reaching to desired numberOfInputs
for i in range(numberOfInputs):
    #take the ith coordinate and split it with comma
    coordinate = input("Enter the " + " coordinate " + str(i+1) +  " (in the form of x,y):").split(',')
    #convert the string inputs to float numbers
    coordinate[0] = float(coordinate[0])
    coordinate[1] = float(coordinate[1])
    #add inputs to list by converting to tuple
    inputs.append(tuple(coordinate))
#initial values    
xCenter = 0
yCenter = 0

for i in range(numberOfInputs):
    #add all x and y values
    xCenter = xCenter + inputs[i][0]
    yCenter = yCenter + inputs[i][1]
#calculate the xCenter and yCenter by dividing with numberOfInputs   
xCenter = xCenter / numberOfInputs
yCenter = yCenter / numberOfInputs
#store the result in a tuple
centerOfMass = xCenter,yCenter
#print it
print("Center of mass = " + str(centerOfMass))
#initial list
distanceList = []
#calculate distance to center for all coordinates
for i in range(numberOfInputs):
    #Euclidean distance formula
    distance = sqrt(pow((inputs[i][0] - xCenter),2) + pow((inputs[i][1] - yCenter),2))
    distanceList.append(distance)  #append to list
#initial values to store the index of the coordinates which are farhest and closest to center
minIndex = 0
maxIndex = 0
max = 0
min = 0
#compare first two coordinates to decided temporary max and min values
if(distanceList[0] > distanceList[1]):
    max = distanceList[0]
    min = distanceList[1]
    maxIndex = 0
    minIndex = 1
else:
    max = distanceList[1]
    min = distanceList[0]
    maxIndex = 1
    minIndex = 0
    
    
#for all inputs compare distances with max and min values
for i in range(numberOfInputs):
    #if distance > max then max = distance
    if(distanceList[i] > max):
        max = distanceList[i]
        maxIndex = i
    #elif distance < min then min = distance
    elif(distanceList[i] < min):
        min = distanceList[i]
        minIndex = i
#print the results
print("The coordinate farthest from the center of mass = " + str(inputs[maxIndex]) + ". Its distance to center = " + str(distanceList[maxIndex]))
print("The coordinate closest from the center of mass = " + str(inputs[minIndex]) + ". Its distance to center = " + str(distanceList[minIndex]))


  



    
