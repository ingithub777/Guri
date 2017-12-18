list_number=input('3개의 값을 입력하세요.:').split()
## 15 3 5

first_num=[]
second_num=[]
list_number[0]=int(list_number[0])
list_number[1]=int(list_number[1])
list_number[2]=int(list_number[2])

for i in range(1,list_number[0]+1):
    if i * list_number[1] <= list_number[0]:
        first_num.append(i*list_number[1])
    if i * list_number[2] <= list_number[0]:
        second_num.append(i*list_number[2])

# sum=set(first_num) | set(second_num)
first_num=set(first_num)
second_num=set(second_num)

sum=first_num | second_num
sum=list(sum)

num=0
for i in sum:
    num+=i
print("0부터 %s 이하의 범위를 선택하셨습니다. 이중에서" % list_number[0])
print("%s의 배수는 %s 입니다." % (list_number[1], first_num))
print("%s의 배수는 %s 입니다." % (list_number[2], second_num))
print("따라서 0부터 %s 이하의 범위내에서 %s 와 %s의 배수의 총합은 %d입니다." % (list_number[0], list_number[1], list_number[2], num))