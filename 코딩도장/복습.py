# 1부터 10까지의 숫자 중 5를 제외한 나머지를 순서대로 출력하세요.
# (2가지 이상의 다른 방법으로 풀어보세요.)

# for i in range(1,5):
#     print(i)
# for i in range(6,11):
#     print(i)

# a = []
# for i in range(1,11):
#     a.append(i)
# b = a[0:4]+a[5:10]
# print(b)

# a = []
# for i in range(1,11):
#     a.append(i)
# a.remove(5)
# print(a)

# for i in range(1,11):
#    if i==5:
#       i+=1
#    print(i)

# 난이도 최하
#
# 사각형을 그리세요
#
# ex)입력 : 3
#
# ***
# *#*
# ***
#
# 입력 : 5
#
# *****
# *###*
# *###*
# *###*
# *****

# a = int(input("숫자를 입력하세요: "))
# for j in range(a):
#     i = '*'
#     if j == 0 or j == a-1:
#         print(i*a)
#     else:
#         print(i+" "*(a-2)+i)


# 난이도 하
# 재귀호출로 1부터 10까지 더하는 프로그램 만들기
# sum 함수안에 내용을 채워넣으세요. 그 이상의 함수 사용불가, for문 while문 등의 반복문 사용 불가능
#
# def sum(num):
#     if num == 10:
#         return num
#     else:
#         return sum(num+1)+num
#
# num = 1
# print(sum(num))
#
# 다음 완성된 코드를 보고 수행결과를 정확히 예측하세요.(인덱스 오류가 될수도 있음)
# 문제를 풀기 전까지 절대 이 코드를 IDE 상에서 실행하지 마세요.
#
# data=[[1,2],[3,4],[5,6],[7,8],[9,10]]
#
# for i in range(5):
#     for j in range(5,0,-1):
#         print(i, end="ㅇ")
#     del data[i][1]
#     print()
#
# for i in data:
#     print(i)

# a라는 리스트에 conv_num 함수를 거쳐 절대값이 된 요소를 출력하는 프로그램을 만드세요
# abs 함수 사용금지
#
# def conv_num(data):
#     if 0 > num[i]:
#         num[i] = -num[i]
#     elif 0 < num[i]:
#         pass
#     print(num[i])
#
# num=[3,-4,5,-6,7,-8]
#
# a=[]
# for i in range(len(num)):
#    conv_num(num[i])

# 다음과 같이 data라는 리스트와 짜다 만 프로그램이 있다.
# 이 리스트에서 찾을 수 없는 요소를 찾을 때에 대한 처리를 만드시오.
# (찾을 수 없을 때에는 반드시 찾을 수 없다는 메세지'만' 나와야 합니다.)
# 이 소스코드를 훼손하지 않는 범위 내에서 프로그램을 작성하세요.(추가나 삽입은 가능, 수정 불가)
# (파이썬에서 자체 제공하는 함수는 주어진 소스코드에 있는 함수만으로 제한)
# ex) (find_num이 10이라고 가정)
# 10을(를) 찾을 수 없습니다.

data= [1,3,5,7,9,11,13,15,17,19]

find_num = 2

for i in range(len(data)):
    if find_num == data[i]:
        print("찾았다!")
        break
    elif find_num != data[i]:
        print("%d을(를) 찾을 수 없습니다." % find_num)
