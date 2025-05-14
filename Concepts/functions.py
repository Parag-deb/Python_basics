# no input , no return
def my_first_fubction():
     a = 10
     b= 12
     print(a+b)

my_first_fubction()
 
# input , no return
def add_two_num(a,b):
     print(a+b)

add_two_num(5,10)
add_two_num(15,10)

#input , return

def mul_two_num(a,b):
     return a*b

result = mul_two_num(12,2)
print(result)

#no input , return

def hello():
     return "hello!!"

greetings = hello()
print(greetings)