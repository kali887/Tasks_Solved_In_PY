# Mostafa Ahmed Magd Ali
# 20230551
# 23/2/2024
# Print a welcome message and explain the purpose of the program
print("Dear user, welcome to our program and thank you for choosing it.")
print("This program is a tool to help you to check if the lists are equal or not.")
print()
def A_1():
    global First_list
    while True:
        First_list = input("Please enter the element of first list :: If you want second list type next: ")
        print()
        if First_list == "next":
            break
        try:
            First_list = int(First_list)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
def A_2():
    global Second_list
    while True:
        Second_list = input("Please enter the element of second list :: If you want to stop type stop: ")
        print()
        if Second_list.lower() == "stop":
            break
        try:
            Second_list = int(Second_list)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
def list__2():
    print()
    global second2_list
    second2_list=[]
    while True:
        A_2()
        if Second_list == "stop":
            break
        second2_list.append(Second_list)


print()
first1_list = []
while True:
    A_1()
    if First_list == "next":
        list__2()
        break
    first1_list.append(First_list)
counter1=0
counter2=0
counter3=0
for i in first1_list:
    counter1+=1
for j in second2_list:
    counter2+=1
if counter1==counter2:
    for i in first1_list:
        for j in second2_list:
            if i == j:
                counter3+=1
                if counter1==counter3:
                    print("The lists are the same")
                    quit()
else:
    print("The lists are not equal")