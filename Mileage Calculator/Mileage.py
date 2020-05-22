print("#### This program gives you the value of X Km for Y Litres of petrol####")
print("                     #### Prices are in INR ####")

user_petrol = input("\nFor how many rupees you filled petrol in your bike? : ")


def petrol(user_petrol):
    """Gives rounded petrol in 1f (In litres)"""
    current_price = 75.54
    petrol_in_litres = (1/float(current_price)) * int(user_petrol)
    rounded_petrol = ("{:.1f}".format(petrol_in_litres))
    return rounded_petrol


def odo():
    """Returns KM driven by users odo inputs"""
    initial_odo = input("Please enter the initial odo reading : ")
    final_odo = input("Enter the final odo reading : ")
    total_km_driven = float(final_odo) - float(initial_odo)
    rounded_tkd = ("{:.1f}".format(total_km_driven))
    return rounded_tkd


petrol_rounded = petrol(user_petrol)
km_driven = odo()
print(f"For {petrol_rounded} litres of petrol, You've driven for about {km_driven} Km.")
print("(Note : The above values are given, considering that your fuel tank is empty.)")



