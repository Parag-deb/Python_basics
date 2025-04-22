a = 'this is a string'

print(a)
print(type(a))
print(a.upper())
print(a)

print(len(a)) #length

print(a[len(a)-1])
print(a[-1])

#python is immutable, string declare hole r change kora jay na

b = 'DINgo'
print(b.swapcase())

#sreing format
age = 23
birthday = '20 February'
user_input = input("What is your name?")
print("Hello, " + user_input + "!")

txt = "I'm {user_input}. I'm {age} years old . My birthday is on {birthday}".format(user_input=user_input , age = age , birthday=birthday)
print(txt)

#f string
print(f"I'm {user_input}. I'm {age} years old. My birthday is on {birthday}")