f=open("E:\새 폴더\새파일.txt",'r')
#print(f.read()) 내용 전체를 문자열로 리턴한다.
lines = f.readlines()

for line in lines:
    print(line)
f.close()
