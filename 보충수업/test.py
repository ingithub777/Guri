while True:
    choice = input("""메뉴를 선택하세요
1. 덧셈
2. 뺄셈
3. 곱셈
4. 나눗셈
0. 종료
번호를 입력하세요: """)
    a = int(input("첫번째 수를 입력하세요: "))
    b = int(input("두번째 수를 입력하세요: "))
    if choice == '0':
        print("종료하겠습니다.")
        break
    elif choice == '1':
        print(a,'+',b,'는',a+b,'입니다.')
    elif choice == '2':
        print(a,'-',b,'는',a-b,'입니다.')
    elif choice == '3':
        print(a,'*',b,'는',a*b,'입니다.')
    elif choice == '4':
        print(a,'/',b,'는',a/b,'입니다.')