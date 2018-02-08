import threading
import time

class MyThread(threading.Thread): # 스레드를 클래스로 정의할 경우에는 __init__메서드에서 부모 클래스의 생성자를 반드시 호출해야한다.
    def __init__(self,msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True # false로하면 죽어도 데몬은 계속돌아간다.

    def run(self): # 반드시 들어가야한다. (run)
        while True:
            time.sleep(1)
            print(self.msg)

# def say(msg):
#     while True:
#         time.sleep(1)
#         print(msg)

for msg in ['you','need','python']:
    t = MyThread(msg)
    t.start()
    # t = threading.Thread(target=say,args=(msg,))
    # t.daemon = True
    # t.start()

for i in range(100):
    time.sleep(0.1) # 시간조절 초단위로 (0.1초도 가능)
    print(i)