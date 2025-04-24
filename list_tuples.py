# list -> we can store different data types
# list is mutable , so we can change any data
a = [1,2,3, 'Naim', 'Fahim', 8.9, 3.4]

print(a)

a[0] = 100

print(a)

s = "he llo"
print(list(s))

a.append([1,2,3])
print(a)
print(a.index('Naim'))

a.reverse()
print(a)

#tuple -> immutable

t = (1,2,3)

#t[0]= 100

print(t)
t_r = tuple(reversed(t))
print(t_r)