
#Car Salesman Program

#Demonstratethe the total cost of car purchase based on
#the stated price of the car

#Write a Car Salesman program where the user enters the base price of a car.
#The program should add on a bunch of extra fees such as tax, license,
#dealer prep, and destination charge.
#Make tax and license a percent of the base price.
#The other fees should be set values.
#Display the actual price of the car once all the extras are applied.

Car_base_price = int(input("How much in $ would you pay for a Toyota car?"))
tax = 0.25 * Car_base_price
print("The tax amount in $ =", tax)
License = 0.05 * Car_base_price
print("The License amount in $ =", License)
print("Dealer prep $ = 2000")
print("Destination charge $ = 1500")
dealer_prep = int(2000)
destination_charge = int(1500)
input("\nPress the enter key for total amount")
print("Total amount for car in $ = ", Car_base_price + tax + License + dealer_prep + destination_charge)
input("\nPress the enter key to end program")
