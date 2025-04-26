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