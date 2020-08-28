# A program to calculate thee total amount after the interest has been added to it

initial_amount = float(input("Enter the initial amount in your account:"))
time = float(input("Enter the time period over which the interest should be caculated(in years):"))
frequency_of_interest = int(input("Enter the frequency of interest:"))
rate = 0.01

total_amount = initial_amount*(1+(rate/frequency_of_interest))**(frequency_of_interest*time)

print("The total amount after a period of  ",time, 
       "years over an amount of",initial_amount,
       "at a rate of",rate, "is ",round(total_amount))