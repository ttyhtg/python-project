import threading
import time

def loop():
    count = 0
    while count <= 100000000:
        count += 1

start_time = time.time()
# 2个线程执行loop方法

loop()
loop()
# t1 = threading.Thread(target=loop)
# t2 = threading.Thread(target=loop)
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()

end_time = time.time()
run_time = end_time - start_time
print(f"{run_time:.4f}")