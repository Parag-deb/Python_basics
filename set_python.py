# {} 
# unordered -> indexing kore value pawa jabe na
# immutable -> no update
# no duplicates

a =[1,2,2,2,3,4,4,4,5]
s = set(a)
print(s)

#Union & Intersection

a = {1,2,3}
b = {2,3,4}
c = b.intersection(a)
print(c)
d=a.union(b)
print(d)