#example 1: If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print ("Welcome To The Cyberhawks Tip Calculator! ")

total_bill = float(input("What was the total bill? "))
#or
#total_bill = input ("What was the total bill? ")

total_percentage = input ("What percentage tip would you like to give? 10,12, or 15? " )
total_people = input ("How many people to split the bill with? ")

#Another formula for answer
# bill_with_tip = (total_percentage / 100 * total_bill + total_bill
#Then divide by amount of people

calc_1 = (int(total_bill) * int(total_percentage))

percent_calc = int(calc_1 / 100)

final_bill = (int(percent_calc) + int(total_bill))

bill_divide = (int(final_bill) / int(total_people))


answer = ("%.2f" % bill_divide)
print (f"Each perosn should pay: ${answer}")


