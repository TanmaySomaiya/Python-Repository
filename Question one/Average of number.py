#asking user how many numbers they want to add
total_numbers=int(input("How many numbers you want to insert: "))

#a variable to store the total of the entered numbers
sum=0

#for loop to take all numbers 

for i in range(total_numbers):
    total=int(input("Enter the number: "))#9
    sum=sum+total
    # a=total#a=9
    # total=a+total#total=9+9
print(sum)
'''
How for loop works here ?
-for loop here will work till the range of numbers that a user wants to add (eg: 2)
-loop will run until all the numbers are added(loop will run 10 times asking for 2 inputs)
-as the total was initalized zero new number added up will be added to the variable

'''
#average formula (that is, the average number will store the quotient of the total divided by total number of input)
average=sum/total_numbers
print("Average of the numbers is: ",average)
#printing the average with the desired message