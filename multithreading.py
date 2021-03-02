






import threading


def printCube(n):

    print("cube is :{}".format(n*n*n))

def printSquare(n):

    print("square is {}".format(n*n))

if __name__ == '__main__':
    t1=threading.Thread(target=printSquare,args=(10,))
    t2=threading.Thread(target=printCube,args=(10,))

    t1.start()#starting thread 1
    t2.start()#starting thread 2

    t1.join() # wait until thread 1 is completely executed
    t2.join() ## wait until thread 2 is completely executed

    print("Done")
