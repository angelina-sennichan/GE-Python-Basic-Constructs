list_values = input("Enter the list of values separated by commas: ").split(",")
number = input("Enter number to check in list: ")

if number in list_values:
    print("True")
else:
    print("False")
