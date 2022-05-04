import time
from threading import Thread


def remind():
    print("Напоминание")
    text = str(input())
    print("Через сколько минут?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    print(text)


th = Thread(target=remind, args=())

th.start()

time.sleep(20)
print("Тут можно делать что угодно, пока поток работает.")
