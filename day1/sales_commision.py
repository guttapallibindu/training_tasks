#sales man comission caluclator 
sales_id = int(input("enter id :")) #takes the id and stores in sales_id
value = float(input("value of sales : ")) #takes amount and stores in value

if value <= 10000 :
    commision = 0
elif value > 10000 and value <= 50000 :
    comission = value * 0.1
elif value >50000 and value <= 100000 :
    comission = value * 0.15
else:
    comission = value * 0.2
print(f"salesman id:{sales_id}, commision: {comission}")