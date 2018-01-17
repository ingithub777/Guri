import math

m = int(input('총건수: '))
n = int(input('한페이지에 보여줄 게시물수: '))

print(math.ceil(m/n))