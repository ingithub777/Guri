import json

student = []

while True:
    student_management = input("(1. 학생정보입력, 2. 학생정보조회, 3. 학생정보수정, 4. 학생정보삭제, 5. 프로그램 종료) : ")
    if student_management == '5':
        break
    elif student_management == '1':
        student_information = [
            {
            'student_ID':input("학생 ID는? : "),
            'name': input("성함은? : "),
            'age': input("나이는? : "),
            'address': input("주소는? : "),
            'lecture_information':
                {
                'past_lecture_number': input("과거수강횟수는? : "),
                'recent_lecture_subject':
                    [
                    {
                    'lecture_code':input("강의코드는? : "),
                    'lecture_name':input("강의명? : "),
                    'teacher':input("강사는? : "),
                    'start_day':input("개강일은? : "),
                    'close_day':input("종료일은? : ")
                    }
                    ]
                }
            }
        ]

        student.append(student_information)
        student_ID = student_information[0].get('student_ID')
        name = student_information[0].get('name')
        age = student_information[0].get('age')
        address = student_information[0].get('address')
        lecture_information = student_information[0].get('lecture_information')
        past_lecture_subject = student_information[0].get('lecture_information').get('past_lecture_subject')

        print(student_ID,name,age,address,lecture_information,past_lecture_subject)
