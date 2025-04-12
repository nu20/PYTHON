def get_input_recursively():
    """
    Recursively takes integer input from the user until a negative number is entered.
    """
    try:
        num = int(input("Enter an integer: "))
        if num < 0:
            return  
        else:
            print("You entered:", num)
            get_input_recursively()  
    except ValueError:
        print("Invalid input. Please enter an integer.")
        get_input_recursively()
get_input_recursively()
print("Negative number entered. Input process stopped.")
