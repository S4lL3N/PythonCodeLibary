import time
import threading
import concurrent.futures

start = time.perf_counter()

def doSomething(seconds):
    print(f"sleeping for {seconds} second(s)")
    time.sleep(seconds)
    print("done sleeping")

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(doSomething, 1)
    f2 = executor.submit(doSomething, 1)

"""
older way of threading 

t1 = threading.Thread(target=doSomething)
t2 = threading.Thread(target=doSomething)

t1.start()
t2.start()

t1.join()
t2.join()

# create a list of threads 
threads = []

for _ in range(10):
    t =threading.Thread(target=doSomething, args=[1.5])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
"""
finish =time.perf_counter()

print(f'\nFinished in {round(finish - start,2)} second(s) ')