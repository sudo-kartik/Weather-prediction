def menu():
    print("*" *45)
    print("-"*5 + " What would you like to do? " + "-" * 5)
    print("\n")
    print("1. Train the model.")
    print("2. Predict the temperature on a specific day?")
    print("\n")

    chose = input("Select option: ")

    while True:
        if chose == 1:
            traing()
        else:
            predict_temp()
        
menu()
