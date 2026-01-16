products = input("Enter list of products separated by commas: ").split(",")
prices = input("Enter list of product prices separated by commas: ").split(",")

product_dict = dict(zip(products, prices))
print(product_dict)
