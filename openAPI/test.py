import json

student_information = []
student_result = []

while True:
    student_management = input("""<< json기반 주소록 관리 프로그램 >>
1. 학생 정보입력
5. 프로그램 종료
    입력 : """)
    if student_management == '5':
        break
    elif student_management == '1':
        try:
            with open('ITT_Student.json', 'r', encoding='utf8') as outfile:
                readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
            student_information = [
                {
                'student_ID': "ITT" + '{:0=3}'.format(len(student_information)+1),
                'name': input("성함은? : ")}
            ]
            student_result.append(readable_result)
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(student_result)
                print('ITT_Student.json SAVED')

        except FileNotFoundError:
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(student_result, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('파일 없다. 파일 생성!!!!!!!!! 가즈아!!!!!!!!!!!!')

# with open('ITT_Student.json','w',encoding='utf8') as outfile:
#     readable_result=json.dumps(student_result,indent=4,sort_keys=True,ensure_ascii=False)
#     outfile.write(readable_result)
#     print('ITT_Student.json SAVED')
