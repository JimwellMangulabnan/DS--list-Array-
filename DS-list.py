# Write a python program that do the following:
# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array

# Note:
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 9:00pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

print("*********  PROGRAMMED BY  ********")
print("***** JIMWELL L. MANGULABNAN *****")
print("********** BSCOE 2-2 *************")

def print_menu():
    print(
     """
----------------------------------------
|       What would you like to do?     |
|--------------------------------------|
| Menu:                                |
|    1 -> Add an element               |
|    2 -> Insert an element            |
|    3 -> Modify an element            |
|    4 -> Delete an element            |
|    5 -> Arrange in ascending order   |
|    6 -> Arrange in descending order  |
|    7 -> Exit                         |
----------------------------------------
    """)
print_menu()

array = [11, 22, 2, 10, 18, 5, 28, 21, 26, 25]
count = 0
while True:
    print("Array:" + str(array))
    choice = int(input("What would you like to do?: "))

    if choice == 1:
        print("\n\t\t| Add an element |\n")
        try:
            element = int(input("Enter the element you want to add: "))
        except ValueError:
            print("\nInvalid")
        else:
            array.append(element)
            print("This is the new array: Array: ", array)

        print_menu()

    elif choice == 2:
        print("\n\t\t| Insert an element |\n")
        try:
            index = int(input("Enter the index number you want to insert: "))
            element = int(input("Enter the element: "))
        except ValueError:
            print("\nInvalid")
        else:
            array.insert(index, element)
            print("This is the new array: Array: ", array)

        print_menu()

    elif choice == 3:
        print("\n\t\t| Modify an element| \n")
        print("Array: ", array)
        try:
            index = int(input("Enter the index you want to modify: "))
            element = int(input("Enter an element you want to add: "))
        except ValueError:
            print("\nInvalid")
        else:
            array[index] = element
            print("This is the new array: Array: ", array)

        print_menu()

    elif choice == 4:
        print("\n\t\t| Delete an element |\n")
        print("Array: ", array)
        try:
            index = int(input("Enter the index you want to delete: "))
        except ValueError:
            print("\nInvalid")
        else:
            array.remove(array[index])
            print("The element has been deleted")
            print("This is the new array: Array: ", array)

        print_menu()

    elif choice == 5:
        print("\n\t\t| Arrange in ascending order |\n")
        print("Array: ", array)
        array.sort()
        print("This is the new array: Array: ", array)

        print_menu()

    elif choice == 6:
        print("\n\t\t| Arrange in descending order |\n")
        print("Array: ", array)
        array.sort()
        array.reverse()
        print("This is the new array: Array: ", array)

        print_menu()

    elif choice == 7:
        print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $                                 $
    $           Thank You             $
    $    For Using The Program!!!     $
    $                                 $
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
    """)
        exit()
        break

    else:
        print("\nInvalid input.")
        break
