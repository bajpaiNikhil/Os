
import threading

x = 0

def increment():
    global x
    x += 1

def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()

def main_task():
    global x

    x = 0


    lock = threading.Lock()# creating a lock


    t1 = threading.Thread(target=thread_task, args=(lock,)) # creating threads
    t2 = threading.Thread(target=thread_task, args=(lock,))


    t1.start()#start threads
    t2.start()


    t1.join()# wait until threads finish their job
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i ,x))