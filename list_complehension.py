a =[1,10,23,24,26,90]

result = []

for i in a :
    if i%2 == 0:
        result.append(i)

print (result)

# applying list comprehension

new_result =[i for i in a if i%2 ==0]
print(new_result)
