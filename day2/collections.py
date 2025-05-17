#list of items 

list1 = ["car","Bike","Plane","Cycle"] #creating a list of items of same type

list1.append("Bus") #adding an element to the list
print(list1)

list1.remove("Cycle") #removing a particluar element in a list
print(list1)

removed_item = list1.pop(1) #poping an element using indexing
print("Removed Item : ",removed_item)
print(list1)

list1.sort()
print(list1) #sorting the elements

list1.reverse()
print(list1) #reversing the order of the elements

count = list1.count("Bus") #counting the no of times bus is present in list
print(count)

index_of_plane = list1.index("Plane") #getting index of the Plane
print(index_of_plane)



for i in list1:
    print(i) 
    
#===============================================================
#tuple handling

tuple1 = (10,20,45,35,25,10) #creating a tuple with barces

count_item = tuple1.count(10) #counting no of times 10 appeared
print("No of 10's in tuple1 :",count_item)

index_item = tuple1.index(45) #finding the index of the 45 
print("index value of 45 in tuple 1 : ",index_item)

#============================================================

#set

set1 = {"Bindu",21,5.4,10} #creating a set of mutiple data types 
set1.add("VIT") #adding an item to the set1
print(set1)

set1.remove(5.4) #removing an particular element
print("after removing and element , set1 : ",set1)

set1.discard(21) #when we use discard for an element it will remove the element
print("after discarding an element : ",set1)

set1.discard(100) #when we use discard for an element which is not present it will not show error
print("after discarding an element not present :",set1)

set2 = {"Guttapalli" , 5,6,7,10} #creating an another set of multiple data types
union_set = set1.union(set2) #cobining both sets using union 
print("combination of 2 sets using union :",union_set)

intersect_set = set1.intersection(set2) #intersecting the 2 sets
print("after intersection :",intersect_set) 

#===========================================================

#dictionary

#creating an dictionary fro products
product = {1:{"p_name":"earbuds","quantity":2,"price":700},
    2:{"p_name":"earphones","quantity":3,"price":200},
    3:{"p_name":"mobile","quantity":10,"price":22000}
}
print("all the products in the dict :",product)

product_2 = product.get(2) #getting an product by its key
print(product_2)

keys = product.keys() #getting all the keys from the product dict
print(keys)

values = product.values() #getting all the product values
print(values)

product.update({4:{"p_name":"phonecase","quantity":4,"price":150}}) #adding an product
print(product)

removed_product = product.pop(1) #removes an element by key
print(removed_product)

lastremoved_product = product.popitem() #removes the last key value pair
print(lastremoved_product)

product.clear() #removing all elements in teh dict 
print(product)


finding_value = "earbuds"
for item in product:
    if item.get('p_name') == finding_value:
        print(item) 
        









