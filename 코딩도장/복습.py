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