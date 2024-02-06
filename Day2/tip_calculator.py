print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What precentage tip would you like to give? 10, 12, or 15? "))
people_nomber = float(input("How many people to split the bill? "))

tip /= 100
bill = bill + (bill * tip)
result = bill / people_nomber
print(f"Each person should pay: ${round(result,2)}")