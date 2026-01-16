regions = input("Enter list of customers' regions separated by commas: ").split(",") 
unique_regions = sorted(set(regions))
print(unique_regions) 
