#{}
# key value pair
# indexing er sujug nai


a = {'rahim' : 12 , 'karim' : 14 , 'fahim' : 78 , 1:[1,2,3,4] , 2:{3,4,5}}

print(type(a))
for i in a:
    print(i)

print("----")

for i in a.values():
    print(i)


print(a.keys(), a.values())

for k,v in a.items():
    print(f"Key name : {k} , Values : {v}")


print("-----")

a = [1,2,3]
b = ["Mango" , "Banana" , "Apple"]

print(dict(zip(a,b)))

c = dict(zip(a,b))
print(c[1]) # here 1 is the key,& we are accessing with the key



chai_types = {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
print(chai_types)
chai_types["Earl Grey"] = "Citrus"
print(chai_types)

chai_types.pop("Ginger")
print(chai_types)
print(f"poped item: {chai_types.popitem()}")
print(chai_types)
#----dictionary under dictionary
tea_shop ={
    "chai":{'Masala': 'Spicy', 'Ginger': 'Zesty'},
    "Tea" : {"Green": "Mild", "BLack": "Strong"}
}
print(tea_shop)

# to access dictionary
print(tea_shop["chai"])
# to access the elements
print(tea_shop["chai"]["Masala"])

squared_number = {x : x**2 for x in range(101)}
for key, value in squared_number.items():
    print(f"{key}: {value}")


keys = ["Masala", "Ginger", "Lemon"]
print(keys)
default_value = "Delicious"
new_dict = dict.fromkeys(keys , default_value)
print(new_dict)
new_dict = dict.fromkeys(keys , keys)
print(new_dict)