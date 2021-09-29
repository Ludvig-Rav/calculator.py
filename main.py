def menu():
    print("=======================================")
    print("| [Welcome, choose yout calculation  ]|")
    print("| =================================== |")
    print("|    [ 1 ]    [ 2 ]    [ 3 ]      [/] |")
    print("|    [ 4 ]    [ 5 ]    [ 6 ]      [X] |")
    print("|    [ 7 ]    [ 8 ]    [ 9 ]      [-] |")
    print("|             [ 0 ]               [+] |")
    print("| [exit(e)]   [ = ]    [ C ]          |")
    print("=======================================")

def result_menu(result):
    print("=======================================")
    print(f"| [Result:              {result}    ]|")
    print("| =================================== |")
    print("|    [ 1 ]    [ 2 ]    [ 3 ]      [/] |")
    print("|    [ 4 ]    [ 5 ]    [ 6 ]      [X] |")
    print("|    [ 7 ]    [ 8 ]    [ 9 ]      [-] |")
    print("|             [ 0 ]               [+] |")
    print("| [exit(e)]   [ = ]    [ C ]          |")
    print("=======================================\n")

def choose_operation():
    ops_choice = input("")
    if ops_choice == "+":
        return ops_choice
    elif ops_choice == "-":
        return ops_choice
    elif ops_choice == "/":
        return ops_choice
    elif ops_choice == "*":
        return ops_choice
    elif ops_choice == "e":
        return ops_choice
    elif ops_choice == "c":
        return ops_choice
    else:
        print("-->Invalid choice<--")
        return 0

while True:
    menu()
    num1 = float((input("")))
    # try:
    #     if num1 == "c":
    #         print("Calculator cleared")
    #     elif num1 == "e":
    #         print("Thanks for using my calculator, see you next time!")
    #         exit()
    # except ValueError:
    #         print("-->You have entered a invalid symbol, try again<--")
    
    num2 = float((input("")))
    operation = choose_operation()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "c":
        print("Clear calculator!")
    elif operation == "e":
        print("Thanks for using my calculator, see you next time!")
        exit()
    else:
        print("--->Seems that you have entered a invalid symbol, try again<---")
    
    result_menu(result)
    print("[||||||||||||||||||||||||||||||||||||||]\n")
    
