print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age > 18 and age < 45:
        bill = 12
        print("Adult tickets are $12.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have free ride on us!")

    with_photo = input("is with photo? Y/N ")
    if with_photo.upper() == 'Y':
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")