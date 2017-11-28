Python 함수

a = [1,2,3,4,5]
a.insert(a,b) - a번째에 b삽입
ex) a.insert(1,9)
a= [1,9,2,3,4,5]
ex) a.append([8.9])
a.extend([]) -  리스트만 추가 가능, 맨 마지막에 추가
ex) a.extend([8.9]) = a+=[4,5], a= a+ [4,5]
a = [1,2,3,4,5,8,9]

a=[1,2,3,1,2,3]
del a[x] [x]번째 요소를 삭제
ex) del a[1]
a = [1,3,1,2,3]
a.remove(x) - 리스트에서 첫번째로 x 제거
ex) a. remove(1)
a = [2,3,1,2,3]
a.pop(x) = x번째 요소를 돌려주고 요소 삭제
