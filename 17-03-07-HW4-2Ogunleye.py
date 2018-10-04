#**********************************************************
#class: IT-512 Spring 2017
#Author: Samson Ogunleye
#Due Date: 03/07/2017
#Assignment-Number: HW4
#Assignment Description: Program is written to sum even numbers using while loop.
#
#
#
#Ver no.         Name(Initials)     Date			Description
#========     ===========    ==========		===============
#
#**********************************************************
#Variable Initialization
#Enter a number
f_number = int(input('Enter an even number: '))
while f_number % 2 != 0:
    print('This is not an even number')
    f_number = int(input('Enter an even number: '))
q_user = 'yes'

#Ask user if he/she wants to enter a new number
q_user = input('Do you want to enter a new number? ')

#Asks the user to input a number
if q_user == 'yes':
    while q_user == 'yes':
        s_number = int(input('Input a number: '))

#If the number is even, it adds this number to previously entered even number
        if s_number % 2 == 0:

#sum = f_number + s_number
          sum = f_number + s_number  

#displays the total
          print(f_number, '+', s_number, '=', sum)

#If it is not an even number is not
        elif s_number % 2 != 0:

#it displays "It is not an even number"
            print('It is not an even number')

#the program asks if you want to enter another number
        q_user = input('Do you want to enter a new number? ')

#If no, then the program will terminate
else:
    print('BYE!!!')
