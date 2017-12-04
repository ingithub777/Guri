def sum_and_mul(a,b):
    return a+b,a*b
result = sum_and_mul(3,4)
print(result)

sum,mul=sum_and_mul(3,4)

print(sum)
print(mul)

#def sum_and_mul(a,b):
#    return a+b
#    return a*b
#result=sum_and_mul(2,3)
#print(result) 리턴을 두개 하는것은 어리석은 짓이다. 처음 리턴값만을 불러온다.
