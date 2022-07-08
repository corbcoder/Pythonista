# Start date - 04/07/2022
# Achieve date - 06/07/2022
#Demonstrate ability to make choice of car based on amount entered.
#Challenge: Write a program to help in deciding where you are in your car purchase journey.

Choice = int(input("Suggest an amount you would spend to buy a car between 1-100,000 \n\t\t$"))

# Cleaned up this section to print less things to the screen
Toyota_Yaris_base_price=10000
tax = 0.15 * Toyota_Yaris_base_price
License = 0.05 * Toyota_Yaris_base_price
Dealership = 0.10 * Toyota_Yaris_base_price
Delivery_charge = 0.02 * Toyota_Yaris_base_price
Total_cost_Yaris = Toyota_Yaris_base_price + tax + License + Dealership + Delivery_charge

# Cleaned up this section to print less things to the screen
Toyota_Avensis_base_price=25000
tax = 0.15 * Toyota_Avensis_base_price
License = 0.05 * Toyota_Avensis_base_price
Dealership = 0.10 * Toyota_Avensis_base_price
Delivery_charge = 0.02 * Toyota_Avensis_base_price
Total_cost_Avensis = Toyota_Avensis_base_price + tax + License + Dealership + Delivery_charge

# Still hoping to improve this section as i make advances in this language.
# Need to find a way to shorten these decision codes
if 1<Choice<10000:
    print("\nYou need to double your hustle, men!")
if 10001<Choice<13199:
    print("\nHmmm, it seems like you are almost there, just a little more hustling and a Toyota is on its way!")
if 13200<Choice<15000:
    print("\a")
    print("\nYou just bought yourself a brand-new Toyota Yaris, smile 'You are the MAN!'")
if 15001<Choice<25000:
    print("You have gotten yourself a Toyota Yaris, \nbut you are on your way to driving a bigger & better Toyota brand. \nKeep the hustle up!")
if 25001<Choice<32999:
    print("\nWow! You so close to buying your dream Toyota Avensis. \nJust a little more hustling and you will be there!")   
if 33000<Choice<40000:
    print("\nHey! you just bought your dream car, Toyota Avensis.", "\tHURRAY!"*10)
if 40001<Choice<100000:
    print("\nMen! move to bigger cars, you don pass Toyota level!")
input("\nPress the enter key to end program")

             
