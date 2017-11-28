old=0
money=0
card=0
fticket = 3
dticket = 5
ticket = 0
while True:
    old=int(input("나이를 알려주세요: "))
    if old <=3:
         print("귀하는 유아 등급이며, 무료입니다.")
    elif 4 <= old <= 13:
        print("귀하는 어린이 등급이며, 2000원입니다.")
        pey=int(input("1: 현금, 2: 카드 선택해주세요 : "))
        if pey == 1:
            money = int(input("요금을 넣어주세요: "))
            if money == 2000:
                print("감사합니다. 티켓을 발행합니다.")
                ticket = ticket + 1
                if ticket % 7 == 0:
                    fticket = fticket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
                if ticket % 4 == 0:
                    dticket = dticket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
            elif money > 2000:
                print("거스름돈 %d를 주고 감사합니다. 티켓을 발행합니다." % (money-2000))
                ticket = ticket + 1
                if ticket % 7 == 0:
                    fticket = fticket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
                if ticket % 4 == 0:
                    dticket = dticket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
            elif money < 2000:
                print(2000-money, "가 모자랍니다." "입력하신",money,"를 반환합니다.")
        elif pey == 2:
            print(2000*0.9,"원 결제되었습니다. 티켓을 발행합니다.")
            ticket = ticket + 1
            if ticket % 7 == 0:
                fticket = fticket-1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓",[fticket],"장")
            if ticket % 4 == 0:
                dticket = dticket-1
                print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓",[dticket],"장")
    elif 14 <= old <= 18:
        print("귀하는 청소년 등급이며, 3000원입니다.")
        pey=int(input("1: 현금, 2: 카드 선택해주세요 : "))
        if pey == 1:
            money = int(input("요금을 넣어주세요: "))
            if money == 3000:
                print("감사합니다. 티켓을 발행합니다.")
                ticket = ticket + 1
                if ticket % 7 == 0:
                    fticket = fticket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
                if ticket % 4 == 0:
                    dticket = dticket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
            elif money > 3000:
                print("거스름돈 %d를 주고 감사합니다. 티켓을 발행합니다." % (money-3000))
                ticket = ticket + 1
                if ticket % 7 == 0:
                    fticket = fticket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
                if ticket % 4 == 0:
                    dticket = dticket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
            elif money < 3000:
                print(3000-money, "가 모자랍니다." "입력하신",money,"를 반환합니다.")
        elif pey == 2:
            print(3000*0.9,"원 결제되었습니다. 티켓을 발행합니다.")
            ticket = ticket+1
            if ticket % 7 == 0:
                fticket = fticket-1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓",[fticket],"장")
            if ticket % 4 == 0:
                dticket = dticket-1
                print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓",[dticket],"장")
    elif 19 <= old <= 59:
        print ("귀하는 성인 등급이며, 5000원입니다.")
        pey = int(input("1: 현금, 2: 카드 선택해주세요 : "))
        if pey == 1:
            money = int(input("요금을 넣어주세요: "))
            if money == 5000:
                print("감사합니다. 티켓을 발행합니다.")
                ticket = ticket + 1
                if ticket % 7 == 0:
                    fticket = fticket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
                if ticket % 4 == 0:
                    dticket = dticket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
            elif money > 5000:
                print("거스름돈 %d를 주고 감사합니다. 티켓을 발행합니다." % (money-5000))
                ticket = ticket + 1
                if ticket % 7 == 0:
                    fticket = fticket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
                if ticket % 4 == 0:
                    dticket = dticket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
            elif money < 5000:
                print(5000-money, "가 모자랍니다." "입력하신",money,"를 반환합니다.")
        elif pey == 2:
            print(5000*0.9,"원 결제되었습니다. 티켓을 발행합니다.")
            ticket = ticket+1
            if ticket % 7 == 0:
                fticket = fticket-1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓",[fticket],"장")
            if ticket % 4 == 0:
                dticket = dticket-1
                print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓",[dticket],"장")
    elif 60 <= old <= 65:
        print("귀하는 성인 등급이며, 5000원입니다.")
        pey = int(input("1: 현금, 2: 카드 선택해주세요 : "))
        if pey == 1:
             money = int(input("요금을 넣어주세요: "))
             if money == 5000:
                print("감사합니다. 티켓을 발행합니다.")
                ticket = ticket + 1
                if ticket % 7 == 0:
                    fticket = fticket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
                if ticket % 4 == 0:
                    dticket = dticket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
             elif money > 5000:
                print("거스름돈 %d를 주고 감사합니다. 티켓을 발행합니다." % (money - 5000))
                ticket = ticket + 1
                if ticket % 7 == 0:
                    fticket = fticket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓", [fticket], "장")
                if ticket % 4 == 0:
                    dticket = dticket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓", [dticket], "장")
             elif money < 5000:
                    print(5000 - money, "가 모자랍니다." "입력하신", money, "를 반환합니다.")
        elif pey == 2:
            print(5000*0.85,"원 결제되었습니다. 티켓을 발행합니다.")
            ticket = ticket+1
            if ticket % 7 == 0:
                fticket = fticket-1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓",[fticket],"장")
            if ticket % 4 == 0:
                dticket = dticket-1
                print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.연간 회원 할인 티켓을 발행합니다. 잔여 무료티켓",[dticket],"장")
    elif old >= 66:
            print ("귀하는 노인 등급이며, 무료.")