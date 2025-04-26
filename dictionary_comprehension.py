nums = list(range(0,11))

result = {i: "EVEN" if i%2==0 else "ODD" for i in nums}
print(result)