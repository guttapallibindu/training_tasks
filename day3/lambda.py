add = lambda x,y: x + y
print(add(1,2))

employees = [
    {"name":"john","salary":20000},
    {"name":"mike","salary":15000},
    {"name":"shaun","salary":24000},
    {"name":"anitha","salary":30000}
]

sorted_employees = sorted(employees, key = lambda x:x["name"])
for emp in sorted_employees:
    print(emp)
