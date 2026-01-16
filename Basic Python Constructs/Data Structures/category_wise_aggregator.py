sales_data = [("Electronics", 1000), ("Furniture", 2000), ("Electronics", 1500)]
sales_per_category = {}

for category, amount in sales_data:
    if category in sales_per_category:
        sales_per_category[category] += amount
    else:
        sales_per_category[category] = amount
print(sales_per_category)
