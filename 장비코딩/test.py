import urllib.request
import datetime
import json
import time
import random

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

access_key = "fgNUbFNWdrPsUqf6WsEPlsKYxDQ%2BgzRO2LIXFxVCeb7zMpjnDnIGiVINYnTenSQdMMseq9GIWW4Bkh5%2B7ZNXKA%3D%3D"

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("0. 프로그램 종료")

def check_device_status():
    print("\n난방기 상태: ",end='')
    if(g_Radiator == True): print("작동")
    elif(g_Radiator == False): print("정지")

    print("가스밸브 상태: ",end='')
    if(g_Gas_Valve == True): print("작동")
    elif(g_Gas_Valve == False): print("정지")

    print("발코니 창문 상태: ",end='')
    if(g_Balcony_Windows == True): print("작동")
    elif(g_Balcony_Windows == False): print("정지")

    print("출입문 상태: ",end='')
    if(g_Door == True): print("작동")
    elif(g_Door == False): print("정지")

def print_device_menu():
    print("상태 변경할 기기를 선택하세요. ")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(배란다) 창문")
    print("4. 출입문")

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" % (datetime.datetime.now(), url))
        return None

def getweather(base_date,base_time,nx,ny):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + base_date
    parameters += '&base_time=' + base_time
    parameters += '&nx=' + nx
    parameters += '&ny=' + ny

    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_realtime_weather_info():
    jsonresult = []
    basedate = time.strftime("%Y%m%d", time.localtime(time.time()))
    basetime = time.strftime("%H%M", time.localtime(time.time()))
    basetime = int(basetime) - 100
    basetime = str(basetime)
    nx = "89"
    ny = "91"

    jsondata = getweather(basedate, basetime, nx, ny)
    if (jsondata['response']['header']['resultMsg'] == 'OK'):
        for i in (jsondata['response']['body']['items']['item']):
            jsonresult.append({'baseDate': i['baseDate'],
                               'baseTime': i['baseTime'],
                               'category': i["category"],
                               'fcstDate': i['fcstDate'],
                               'fcstTime': i['fcstTime'],
                               'fcstValue': i['fcstValue'],
                               'nx': i['nx'],
                               'ny': i['ny'] })
    print("%s_%s_날씨정보"%(basedate, basetime))
    with open('%s_%s_날씨정보.json' % (basedate, basetime), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonresult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

def smart_mode():
    global g_AI_Mode
    global g_Balcony_Windows
    print("\n1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태변경")
    print("3. 실시간 기상정보 Update")
    print("4. 강수예보 시뮬레이션")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else: print("정지")
    elif menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")

        else: print("중지")

    elif menu_num == 3:
        get_realtime_weather_info()

    elif menu_num == 4:
        RN1 = random.randint(0, 3)
        if RN1 == 0:
            g_Balcony_Windows = True
            print("창문을 열겠습니다.")
        else:
            print("비가와요! 문닫아요! 창문을 닫습니다.")


def control_device():
    global g_Radiator
    global g_Gas_Valve
    global g_Balcony_Windows
    global g_Door
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1:
        if g_Radiator == True: g_Radiator = False
        elif g_Radiator == False: g_Radiator = True

        if g_Gas_Valve == True: g_Gas_Valve = False
        elif g_Gas_Valve == False: g_Gas_Valve = True

        if g_Balcony_Windows == True: g_Balcony_Windows = False
        elif g_Balcony_Windows == False: g_Balcony_Windows = True

        if g_Door == True: g_Door = False
        elif g_Door == False: g_Door = True

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num == 2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 0): break