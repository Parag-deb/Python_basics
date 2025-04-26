#{}
# key value pair
# indexing er sujug nai
# key gula obossoi immutable

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