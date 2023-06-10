#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentrage tip would you like to give? 10, 12, or 15? "))/100
number_people = int(input("How many people to split the bill? "))

total_with_tip = total_bill * (1 + percentage_tip)
person_pay = round(total_with_tip / number_people, 2)

result = f"Each person should pay: ${person_pay:.2f}"

print(result)



 