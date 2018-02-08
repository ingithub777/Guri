f=open("E:\새 폴더\새파일.txt",'r')
while True:
    line=f.readline()
    if not line: break
    print(line,end='')
f.close()

#있는 파일을 불러오기