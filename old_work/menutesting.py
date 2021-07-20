while True:            
    prompt_start = print("Which type of data do you want to view?")
    try:
        prompt_input = int(input("[1]Temperature \n[2]Humidity \n[3]Carbon Monoxide \n[4]Small PM \n[5]Large PM \n[6]Nitrogren Dioxide \n[0]End Program \nEnter a number (0-6): "))
        if prompt_input == 1:           
            print("Current Temperature")
            try:
                cont = str(input("Do you want to continue? : "))
                if cont == "y" or "Y" or "Yes" or "yes":
                    print("queso")
                elif cont == "n" or "N" or "No" or "no":
                    print("Data Collecting Terminated. \nGoodbye!")
                    break
            except ValueError:
                print("Invalid Input: Answer Y / N")
                
        elif prompt_input == 2:
            print("Current Humidity")
        elif prompt_input == 3:
            print("CO Currently")
        elif prompt_input == 4:
            print("Small PM")
        elif prompt_input == 5:
            print("Large PM")
        elif prompt_input == 6:
            print("Nitrogen Dioxide")
        elif prompt_input == 0:
            print("Data Collecting Terminated. \nGoodbye!")
            break
        else:
            print("Enter a valid number (1-6)")
    except ValueError:
        print("This is not a number")
   
