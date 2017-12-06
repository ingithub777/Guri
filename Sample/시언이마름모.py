while True:
    input2=int(input())
    if input2%2==0 & input2==0:# 입력값이 2로 나눠떨어지고 0이 아닌경우 0이거나 짝수이므로. &input2!=0
        print("홀수를 입력하세요")
        continue
    elif input2==0:#0이 입력되면 무조건 종료.
        print("마름모 프로그램을 이용해 주셔서 감사합니다.")
        break
    else :
        pass
    mid = int(input2 / 2)
    i=1
    count=1
    vertical_bar=0
    while i<=mid+1:
        count=0
        while vertical_bar < input2 :#수평바 그리기
            if vertical_bar==0 : #수평바 그리기 전 한 칸 띄우기
                print('　',end="")
            print('-',end="")
            if vertical_bar+1==input2:#수평바 그린 후 한 칸 띄우기
                print('　',end="")
            vertical_bar+=1
            if vertical_bar==input2:
                print()#수평바 그리기 마무리
        while count < mid + 2 - i:  # blank는 (입력값/2)+1만큼을 항상 필요로 한다.
            if count==0:            # 세로바 그리기
                print('|',end='')   # 세로바 왼쪽부분 그리기
            print(" ", end="")  # count는 0부터 시작해서 blank필요수 만큼만 반복되도록 한다.
            count += 1
        count = 1
        while count <= 2 * i - 1:  # 별을 홀수개로 찍어내야 되니 count가 1부터 시작해야됨.
            print("*", end="")  # (2X1)-1,(2X2)-1,(2X3)-1, ... 이런식으로 홀수개의 별이 출력됨
            count += 1  # count 값이 증가하여 반복문을 탈출할 수 있게.
        count=mid-1   #별을 그린 후에 공백을 추가로 출력해야함
        while count<input2-i:   # 카운트값을 중간으로 두고 중간위치부터 끝까지 공백을 만들어냄
            print(' ',end="")
            count+=1
            if count==input2-i:
                print('|')#,end="")
        i += 1
    # 마름모 상단부분 완성
    i = 1
    while i < mid + 1:  # 별의 증가는 항상 2개씩이므로 입력값의 절반을 최대값으로 둔다. i는 밑의 반복문에서 1의 값이 초기에 필요함
        count = 0  # 따라서 부득이하게 초기값을 1로 잡았고 mid값에도 1을 추가시킴
        while count < i+1:  # 밑의 statement block은 무조건 처음부터 실행되어야 한다. 따라서 i는 0이 아닌 1, count는 0
            if count==0:
                print('|',end="")
            print(" ", end="")
            count += 1
        count = 0
        while count < 2 * (mid - i) + 1:  # 중간값-i을 하면 입력값 7기준 3,2,1,...로 줄어 X2를 하면 얼추 모양이 잡히고
            print("*", end="")  # 여기에 1을 더하면 홀수개의 별이 출력된다.
            count += 1  # 반복문에서 탈출할 수 있도록 count값이 증가
        count=mid       # 별을 모두 찍었으므로 공백 만들 준비를 함

        while count<mid+1+i:# 마름모 하단 공백출력
            print(' ',end="")
            count+=1
            if count==mid+1+i:  #(공백을 다 찍은 상태)
                print('|')
        i += 1
        if i==mid+1:
            vertical_bar=0
            while vertical_bar<input2:
                if vertical_bar==0:
                    print('　',end="")#수평바 그리기 전 한 칸 띄우기
                print('-',end="")
                if vertical_bar+1==input2:
                    print('　',end="")#수평바 그린 후 한 칸 띄우기
                vertical_bar+=1
    if input2==1:
        print('　-　',end="")
        # 마름모 하단부분 완성