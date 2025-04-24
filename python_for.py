for x in range(6):
    print(x)

fruits = ["apple", "banana", "Cherry"]

for x in fruits:
    print(x)


for x in fruits:
    print(x)
    if x =="banana":
        break


print('a'  in "Hello") # answer in false , cause there is no 'a' in hello

print('e' in "Hello")


for i in range(101):
    print(f"Nasa in hacking.. {i}%")
print("hasa in hacked!!")


l =[1,2,3,4,'s', 5, 6, 7]

for i in l:
    if type(i) == type('b'):
        break
    else:
        print(i)

print("for continue -----")
for i in l:
    if type(i) == type('b'):
        continue
    else:
        print(i)