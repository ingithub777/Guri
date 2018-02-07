import re
# 대문자 소문자 구분해야된다.
# p = re.compile('[abc]') # 문자열중에 첫번째 문자가 'a,b,c'랑 매칭이 되느냐
# m = p.match("ability")
# m = p.match("zebra") # 매칭이 안됨
# print(m)

# [a][b] 같은 경우에는 문자열중에 첫번째 문자가 a 두번째 문자가 b가 와야지 매칭이 된다.

# p = re.compile('[e][l][e]')
# p = re.compile('e') # 가능
# p = re.compile('ela') # 불가능
# p = re.compile('[ela]') # 가능
# m = p.match("element")
# print(m)

# p = re.compile('a[abc]c') # 불가능
# m = p.match("aabc")
# p = re.compile('a[abc]c') # 가능
# m = p.match("acc")
# print(m)

# p = re.compile('[a-z]') # 가능 [abcdefghijklmnopqrstuvwxyz] 같은 의미
# m = p.match("a!") # [abcdefghijklmnopqrstuvwxyz] 같은 의미이나 이렇게 하면 매칭은 안됨, [a-z] 가능
# print(m)

# p = re.compile('[a-z,A-Z]')
# m = p.match(",") # 가능
# print(m)
#
# p = re.compile('[a-zA-Z]')
# m = p.match("z") # 가능
# print(m)

# ^ caret의 의미

# p = re.compile('[^a-zA-Z]')
# m = p.match("z") # 불가능
# print(m)
# p = re.compile('[^0]')
# m = p.match("1") # 가능
# print(m)
# p = re.compile('[^\d]')
# m = p.match("k") # 가능
# print(m)

# p = re.compile('[\s]') # 공백문자에 매치
# # m = p.match(" ") # 가능
# m = p.match("") # 불가능
# print(m)
#
# p = re.compile('[\S]') # 공백문자가 아닌것에 매치
# m = p.match(" ") # 불가능
# m = p.match("a") # 가능
# print(m)

# p = re.compile('[\w]') # 문자+숫자에 매치
# m = p.match("1") # 가능
# # m = p.match("*") # 불가능
# print(m)
#
# p = re.compile('[\W]') # 문자+숫자가 아닌것에 매치
# # m = p.match("1") # 불가능
# m = p.match("*") # 가능
# print(m)

# p = re.compile('a.b') # dot(.) 은 a와 b사이에 줄바꿈문자를 제외한 어떤 문자가 들어가도 모두 매치
# m = p.match("ab") # 불가능
# m = p.match("a*b") # 가능
# print(m)

# p = re.compile('a*b') # a가 0번이상 반복이면 매칭
# m = p.match("ab") # 가능
# print(m)

# p = re.compile('a+b') # a가 1번이상 반복이면 매칭
# m = p.match("ab") # 가능
# print(m)

# p = re.compile('a{0,5}b') # 0에서 5번 반복이면 매칭
# m = p.match("ab") # 가능
# print(m)

# p = re.compile('ab?c') # b가 0~1번 사용되면 매치
# m = p.match("ac") # 가능
# m = p.match("abbc") # 불가능
# print(m)

# p = re.compile('[a-z]+') #
# m = p.match("3 python") # 불가능
# m = p.search("3 python") # 가능
# m = p.findall("pythons python!") # 컴파일안에 있는 것들만 리턴
# m = p.finditer("pythons python") # findall과 동일하지만 그 결과로 반복 가능한 객체를 리턴
# print(m)

# p = re.compile("^python\s\w+",re.MULTILINE) # MULTILINE을 쓰게되면 모든 데이타에서 python이 들어간 것을 찾아준다.
# data = """python one
# life is too short
# python two
# you need python
# python three"""
# print(p.findall(data))

p = re.compile(r"(\b\w+)\s+\1")
m = p.search("Paris in the the spring").group()
print(m)