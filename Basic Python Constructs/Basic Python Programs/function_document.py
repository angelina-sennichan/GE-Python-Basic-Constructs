function_name = input("Enter name of a Python built-in function: ")

try:
    function = eval(function_name)
    print(function.__doc__)
except:
    print("Invalid function name")
