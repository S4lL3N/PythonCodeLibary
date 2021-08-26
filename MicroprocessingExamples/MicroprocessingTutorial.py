'''
use multi processing to speed up processing

https://www.youtube.com/watch?v=fKl2JW_qrso&t=1773s
'''
#=====================================================================================================================================
import time
import multiprocessing
import concurrent.futures

if __name__ == '__main__':

    start = time.perf_counter()

    def doSomething(seconds):
        print(f"sleeping... for {seconds} seconds")
        time.sleep(seconds)
        print(f"done sleeping for {seconds}")

    with concurrent.futures.ProcessPoolExecutor() as exector:
        f1 = exector.submit(doSomething(5))
        f2 = exector.submit(doSomething(1))
        
    #doSomething()

    '''creating the processes'''
    #process1 = multiprocessing.Process(target=doSomething())
    #process2 = multiprocessing.Process(target=doSomething())

    '''starting the processes'''
    #process1.start()
    #process2.start()

    '''the join runs the processes and completes them before moving on through the code. if you leave out it will finish the main before running the processes'''
    #process1.join()
    #process2.join()

    """
    #create a list of processes
    processes = []
    #loop through creating a process 10 times
    for _ in range(10):
        p = multiprocessing.Process(target=doSomething())
        p.start()
        processes.append(p)

    for process in processes:
        process.join()   
    """

    finish = time.perf_counter()

    print(f'finished in {round(finish - start, 2)} seconds')


