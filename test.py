import threading
import time


# 定义线程需要做的内容，写在函数里面
def target():
    time.sleep(5)
    print('我是延时器里的')



t = threading.Thread(target=target, args=[])

t.start()
print('正在运行' )