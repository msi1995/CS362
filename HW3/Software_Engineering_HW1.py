while(1):
	year = int(input("Please enter a year. The program will check if the year is a leap year or not: "))
	flag = 0

	if(year%4 == 0):
		flag = 1

	if(year%100 == 0):
		flag = 0

	if(year%400 == 0):
		flag = 1


	if(flag == 1):
		print('The year ', year,' is a leap year.')
	elif(flag == 0):
		print('The year ', year,' is not a leap year.')

	