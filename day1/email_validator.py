#email validator

#creating list of dictonaries that contains employee details
employees = [
    {"name":" Alex Johnson ray" ,"email": "Alex.j@company.com"},
    {"name":"Bob Smith" ,"email": "bob.smith@company.com"},
    {"name":"   carol lee" ,"email": "  carol.lee@otherdomain.com"}
]
for emp in employees: #iterating for every employee
    name = emp["name"].strip() #removing spaces in employee name
    email = emp["email"].strip().lower() #converting all the charectors in email to lower case
    
    indx = email.index("@")
    domain = email
    #validating email
    
    if not email.startswith(name[0].lower()): #checking if email id start with first word of name and in lower case
        print(f"Inavlid email format for {name}  doesn't start with name.")
        continue #skipping that particular iteration 
    
    if "@company.com" not in email: #checking for the correct domain name
        print(f"Invalid domain for {name}: {email}")
        continue #skipping iteration
        
    
    #generating username
    parts = name.lower().split() #converting name into lower and splitting into parts
    if len(parts) >= 2: #if name had 2 or more than 2 parts (first name , second name)
        username = parts[0] + "." + parts[1] #adding first name and . and second name
    else: #if name has only one part
        username = parts[0]
    
        
    print(f"Name: {name} | Email: {email} | Username: {username}") #prints the name , email and username