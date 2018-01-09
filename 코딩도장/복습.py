numbers = int(input('입력할 정수의 개수를 입력하세요 : '))
sum = 0

for i in range(numbers):
    sum += int(input('정수를 입력하세요 : '))

print('입력한 정수의 합은 :', sum, '입니다.')
print('입력한 정수의 평균은 :', sum/numbers, '입니다.')