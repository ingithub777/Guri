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
# * *
# ***
#
# 입력 : 5
#
# *****
# *   *
# *   *
# *   *
# *****

a = input("숫자를 입력하세요: ")
for i in a:
    i = int(i)
    i = '*'*int(a)
    print(i)

난이도
하

재귀호출로
1
부터
10
까지
더하는
프로그램
만들기


def sum(num):
    pass


num = 1

print(sum(num))

sum
함수
안에
내용을
채워넣으세요.그
이상의
함수
사용
불가, for문
while문
등의
반복문
사용
불가능