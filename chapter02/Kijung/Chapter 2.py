Python  함수

a = [1,2,3,4,5]
a.insert(a,b) - a번째에 b 삽입
ex) a.insert(1,9)
a = [1,9,2,3,4,5]
a.append(x,[]) - 어떤 자료형도 추가 가능, 맨 마지막에 추가
ex) a.append([8,9])
a = [1,2,3,4,5,[8,9]]
a.extend([]) - 리스트만 추가 가능, 맨 마지막에 추가
ex) a.extend([8.9]) = a+=[4,5] , a = a + [4,5]
a = [1,2,3,4,5,8,9]

a = [1,2,3,1,2,3]
del a[x] - [x]번째 요소를 삭제
ex) del a[1]
a = [1,3,1,2,3]
a.remove(x) -  리스트에서 첫번째로 x 제거
ex) a.remove(1)
a = [2,3,1,2,3]
a.pop(x) = x번째 요소를 돌려주고 요소 삭제
ex) a.pop(1)
2
a = [1,3,1,2,3]

Python 형태
1) String
a. \를 사용하면 '나 ''를 문자열에 포함시킬수 있다
ex) say = "\"Python is ver easy.\" he says."
Escape code
\n : 문자열 안에서 줄을 바꿀때 사용
\t : 문자열 사이에 탭 간격을 줄 때 사용
\\ : 문자 \를 그대로 표현할 때 사용
\' : 작은따옴표를 그대로 표현할 때 사용
\'': 큰따옴표를 그대로 표현할 때 사용

a.count('x') - x 문자 개수 세기
a.find('x') - x 위치 알려주기 , 존재하지 않는다면 -1 반환
a=","
a.join('abcd') - abcd라는 문자열의 각각의 문자 사이에 변수a의 값인 ","를 삽입하다
a.upper() - 소문자->대문자
a.lower() - 대문자->소문자
a.strip() - 양쪽 공백 지우기
a.replace(a,b) - a를 b로 바꿔줌

Format code: 문자열 내에 어떤 값을 삽입하는 방법
%s : String
%c : Character
%d : integer
%f : floating-point
%% : '%' 자체

2) List - []
a.sort() - 리스트의 요소를 순서대로 정리
a.reverse() - 리스트를 역순으로 뒤집어 준다
a.index(x) - x의 위치값을 리턴한다
a.insert(a,b) - a 위치에 b를 삽입

3) Tuple - () 값을 바꿀수 없다
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))

4) Dictionary - {Key1:Value1, Key2:Value2 ...}
a. 쌍 추가하기
a =  {1:'a'}
a[2] = 'b'
a
{2:'b',1:'a'}
b. 삭제하기
del a[1]
a
{2:'b'}
a.keys() - Key 리스트
a.values() - value 리스트
a.items() - key, value 쌍 얻기
a.clear() - key:value 쌍 모두 지우기

5) Set -{ } => 중복 허용 X, 순서가 없다
   s1 = set([1,2,3])
   s1 = {1,2,3}
   s2 = set("Hello")
   s2 = {'e', 'l', 'o', 'H'}
교집합 : s1 & s2, s1.intersection(s2)
합집합 : s1 | s2, s1.union(s2)
차집합 : s1 - s2, s1.difference(s2)
a.add(x) - x 값 추가하기
a.update(리스트형x) - 여러 값 추가하기
a.remove(x) = 특정 x 값 제거
