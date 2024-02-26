# Mostafa Ahmed Magd Ali
# 20230551
# 23/2/2024
# Print a welcome message and explain the purpose of the program
print("Dear user, welcome to our program and thank you for choosing it.")
print("This program is a tool to help you to calculate Pi.")
x= True
while x== True:
    # Ask the user for the number of terms to use in the approximation
    while True:
        the_n_times = input("How many times? ")
        print()
        try:
            the_n_times = int(the_n_times)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    the_n_times+=1
    # Initialize the total and pi_over_4 variables to zero
    pi_over_4 = 0
    den=1
    # Loop through the number of terms
    print("Pi over 4 is : ", end="")
    for i in range(1,the_n_times):
        # Check if i is even or odd
        if i % 2 == 1:
            # Add the term to pi_over_4 if i is even
            pi_over_4+=1/(den)
            if i == (the_n_times-1):
                print(f"{1}/{den}", end="")
                break
            elif i==1:
                print (f"{1}",end=" - ")
                den += 2
                continue
            print(f"{1}/{den}", end=" - ")
            den += 2
        else:
            # Subtract the term from pi_over_4 if i is odd
            pi_over_4 -= 1 / (den)
            if i == (the_n_times-1):
                print(f"{1}/{den}", end="")
                break
            print(f"{1}/{den}", end=" + ")
            den += 2
        # Add pi_over_4 to the total

    # Multiply the total by 4 to get an approximation of Pi
    print()
    pi = pi_over_4 * 4

    # Print the result
    print("The Pi over 4 is : ", pi_over_4)
    print("The approximation of Pi is", pi)
    again = input("Would you like to play again?(yes/no)")
    if again.lower() == "yes":
        x=True
        print()
    else:
        quit()

