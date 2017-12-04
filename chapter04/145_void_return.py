#def sum(a,b):
#    print("%d, %d의 합은 %d입니다." % (a,b,a+b))
#
#sum(3,4)
#
#a=sum(1,2)
#
#print(a)

def sum_many(*args):
    sum = 0

    for i in args:
        sum = sum + i

    return sum

result=sum_many(1,2,3)
print(result)
#print(sum_many(1,2,3) 한줄로 하기

result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)