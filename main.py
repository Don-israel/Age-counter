def check_age():
    age_input = input("Enter your age: ")

    # Check if the input is an integer
    if age_input.isdigit():
        age = int(age_input)
        
        # Check if the age is odd or even
        if age % 2 == 0:
            print("The age entered is even.")
        else:
            print("The age entered is odd.")
    else:
        print("ValueError: Please enter a valid integer age.")

# Run the function
check_age()
