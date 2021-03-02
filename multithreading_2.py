


import threading
import os

def task1():
    print("Task 1 is assingned to the thread {}".format(threading.current_thread().name))
    print("Process id of the thread(task1) {}".format(os.getpid()))

def task2():
    print("Task 2 is assingned to the thread {}".format(threading.current_thread().name))
    print("Process id of the thread(task2) {}".format(os.getpid()))

if __name__ == '__main__':

    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))
    #We use threading.main_thread() function to get the main thread object.
    # In normal  conditions, the main thread is the thread from which the Python interpreter was started.
    # name attribute of thread object is used to get the name of thread


    t1=threading.Thread(target=task1,name="T1")
    t2=threading.Thread(target=task2,name="t2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("DONE!!!")