import time
from threading import Thread

answer = None

def check():
    time.sleep(5)
    if answer != None:
        return
    print("Too Slow")

Thread(target = check).start()

answer = input("Input something: ")