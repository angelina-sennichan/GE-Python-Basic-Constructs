list1 = input("Enter colors for list 1 separated by commas: ").split(",")
list2 = input("Enter colors for list 2 separated by commas: ").split(",")

color_list_1 = set(list1)
color_list_2 = set(list2)

difference = color_list_1 - color_list_2
print("Colors in list1 not in list2:", difference)
