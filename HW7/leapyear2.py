def checkleap(year):
    flag = 0

    if(year%4 == 0):
        flag = 1


    if(flag == 1):
        return True
    elif(flag == 0):
        return False