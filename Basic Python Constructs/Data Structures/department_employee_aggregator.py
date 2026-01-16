from collections import defaultdict

data = [("IT", "Alex"), ("HR", "Riya"), ("IT", "John")]
employees_by_department = defaultdict(list)
for department, employee in data:
    employees_by_department[department].append(employee)
print(dict(employees_by_department))

