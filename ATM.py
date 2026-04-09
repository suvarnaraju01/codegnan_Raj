SBI_RAJ = {"Name" : "RAJ",
                      "ATM PIN" : "2391",
                      "Balance":5000}
user_pin = input (" Enter Pin: ")
if len(user_pin) == 4:
    if user_pin in SBI_RAJ["ATM PIN"]:
        user_choice = int(input("enter your choice "))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw"))
            if money_w <= SBI_RAJ["Balance"]:
                SBI_RAJ["Balance"] -= money_w
                print ( SBI_RAJ["Balance"])
            else:
                print("Insufficient balance")
        elif user_choice == 2:
             Deposite_M = int(input("pls enter the money you want to deposite"))
             if Deposite_M % 100 == 0 and Deposite_M>=1000:
                 SBI_RAJ['Balance'] += Deposite_M
                 print(f"you have deposite {Deposite_M} and the total  is {SBI_RAJ}")
             else:
                print(f"{Deposite_M} you have entered  is change or less than 5000/-")
        elif user_choice == 3:
            old_pin = input("Enter old pin again: ")
            if old_pin == SBI_RAJ["ATM PIN"]:
                new_pin = input("Enter new pin: ")
                if new_pin != user_pin:
                    SBI_RAJ["ATM PIN"] = new_pin
                    print(f"PIN changed successfully to {new_pin}")
                else:
                    print("Pin should not match old pin")
    else:
            print("You have enetered invalid pin")
else:
    print("Pls enter 4 digit pin")
