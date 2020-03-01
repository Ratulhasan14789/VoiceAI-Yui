import requests
from multiprocessing import Process
def loader(x,y):

    str4 =  b'<html>\r\n<head><title>404 Not Found</title></head>\r\n<body>\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n'

    for i in range(x, y+1):
        str2 = 'https://www.porncomixonline.net/pics/2018/10/Milftoon-Hera-Milftoon-Space-Clones-'+str(i)+'.jpg'
        str3 = 'https://www.porncomixonline.net/pics/2018/10/Milftoon-Hera-Milftoon-Space-Clones-'+str(i)+'.png'


        a= requests.get(str2).content
        if a!=str4:
            ext='.jpg'
            bits=0
        else:
            ext=".png"
            b= requests.get(str3).content
            bits=1
        str1 = 'Hera Milftoon and The Space Clones_'+str(i)+ext
        f = open(str1, 'wb')
        if bits==0:
            f.write(a)
        else:
            f.write(b)
        f.close()
        print(i,'done',end="\r")
def load(a,b):

    b1=b//4
    b2=b//2
    b3=b1*3

    if __name__=="__main__":
        p1=Process(target=loader, args=(a,b1,))
        p2=Process(target=loader, args=(b1,b2,))
        p3=Process(target=loader, args=(b2,b3,))
        p4=Process(target=loader, args=(b3,b,))

        p1.start()
        p2.start()
        p3.start()
        p4.start()

#https://i.nhentai.net/galleries/471851/1.jpg
#load(10,50)