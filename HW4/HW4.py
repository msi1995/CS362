def cubeVolume(side):
    if(side < 0):
        return 0;
    volume = side * side * side
    return volume

def findAvg(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    average = sum/len((array))
    return average

def makeFullName(a, b):
    fullName = a + " " + b
    return fullName
