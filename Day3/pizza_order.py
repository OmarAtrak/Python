size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0

if size.upper() == "S":
  bill = 15
elif size.upper() == "M":
  bill = 20
elif size.upper() == "L":
  bill= 25

if add_pepperoni.upper() == "Y":
  if size.upper() == "S":
    bill += 2
  elif size.upper() == "M" or size.upper() == "L":
    bill += 3

if extra_cheese.upper() == "Y":
  bill += 1


print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}.")

