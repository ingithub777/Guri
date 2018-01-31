import  json

real_weather_list = []
with open('20180131_1615_날씨정보.json', encoding='utf8') as outfile:  # json파일 실제시간으로 수정필요
    json_object = json.load(outfile)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)
real_weather_list.append(json_big_data)
weather_div = real_weather_list[0]
if weather_div[0]['category'] == "REH":
    print(weather_div[0]['fcstValue'])
    print("OK")