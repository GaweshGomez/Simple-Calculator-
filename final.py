def menu():
    print("----------------------------------------------------")
    print("                  WONDER CALCULATOR                 ")
    print("====================================================")
    print("")
    print("                     MAIN STUDY                     ")
    print("")
    print("1. Enter the positive integer numbers")
    print("2. Display Highest value")
    print("3. Display Lowest value")
    print("4. Display Average value")
    print("5. Display even numbers")
    print("6. End")


option = 0
while option!=6:
    menu()
    try:
        print("")
        option = int(input("Enter a option : "))
        if option == 1:
            integer_numbers = []

            print("")
            n = int(input("How many numbers do you want to enter (Maximum value is 10) : "))
            if n <= 10:
                for i in range(0, n):
                    ele = int(input("Enter Number: "))

                    integer_numbers.append(ele)

                print("************************************************************")
                print("Input Numbers are ", integer_numbers)
                print("************************************************************")
                print("")

                choice = "yes"
                while option != 6 and choice != "no":
                    try:
                        print("")
                        choice = input("Do you need to continue with another option ?")
                        while choice == "yes":
                            option = int(input("Enter a option : "))
                            if option == 2:
                                print("Maximum Number is", max(integer_numbers))
                                choice = input("Do you need to continue with another option ?")
                            elif option == 3:
                                print(min(integer_numbers))
                                choice = input("Do you need to continue with another option ?")
                            elif option == 4:
                                avg = (sum(integer_numbers)) / n
                                print(avg)
                                choice = input("Do you need to continue with another option ?")
                            elif option == 5:
                                for no in integer_numbers:
                                    if no % 2 == 0:
                                        print(no, end=" ")
                                        print("")
                                choice = input("Do you need to continue with another option ?")
                            elif option == 6:
                                exit(0)
                            elif option > 6:
                                print("Invalid Input ")

                    except ValueError:
                        print("Value Error! Please Enter a Correct Value ")
                else:
                    exit(0)
            else:
                print("")
                print("!!! attention !!!")
                print("your value should be less than 10 !!!")
    except ValueError:
        print("Value Error! Please Enter a Correct Value ")
