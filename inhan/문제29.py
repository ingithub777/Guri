e2 = 0
while True:
    a = input("범위, 두 수를 입력하세요 : ").split(' ')
    b2 = []
    c2 = []
    for i in range(1,int(a[0])):
        b = int(a[1])*i
        c = int(a[2])*i
        d = b2+c2
        d2 = set(d)
        b2.append(b)
        c2.append(c)
        e = list(d2)
        for k in e:
            e2 += k
    print("""0부터 %s 이하의 범위를 선택하셨습니다. 이 중에서
             %s의 배수는 %s 입니다.
             %s의 배수는 %s 입니다.
             %s와 %s의 배수는 %s입니다.
             따라서 0부터 %s이하의 범위내에서 %s와 %s의 배수의 총합은 %s입니다.""" % (a[0], a[1], b2, a[2], c2, a[1], a[2], d2, a[0], a[1], a[2], e2))
    break
