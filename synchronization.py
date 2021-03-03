#https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
import threading
x = 0

def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1

def thread_task():
    """
        task for thread
        calls increment function 100000 times.
        """
    for _ in range(100000):
        increment()

def main_task():
    global x

    x = 0# setting global variable x as 0


    t1 = threading.Thread(target=thread_task)# creating threads
    t2 = threading.Thread(target=thread_task)


    t1.start()
    t2.start()# start threads


    t1.join()# wait until threads finish their job
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i ,x))


"""The expected final value of x is 200000 but what we get in 10 iterations of main_task function is some different values.

This happens due to concurrent access of threads to the shared variable x. 
This unpredictability in value of x is nothing but race condition."""

"""threading module provides a Lock class to deal with the race conditions. 
    Lock is implemented using a Semaphore object provided by the Operating System."""