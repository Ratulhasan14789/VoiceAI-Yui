from multiprocessing import Process
from os import getppid, getpid

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', getppid())
    print('process id:', getpid())

def f(name):
    info('function f')
    print('hello', name)

info('main line')
 
p = Process(target=f, args=('bob',))
p.start()