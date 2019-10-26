import hashlib

num=0

f= open("Yui_data/RAM/md5-4digits.db", "a")
        

while num<=10050:
    x=str(num)
    if len(x)==1:
        strnum="000"+x
    elif len(x)==2:
        strnum="00"+x
    elif len(x)==3:
        strnum="0"+x
    elif len(x)==4:
        strnum=""+x
    elif len(x)==5:
        strnum="0"+x
    else:
        strnum=x
    xmd5 = hashlib.md5(strnum.encode('utf-8')).hexdigest()
    nummd5="*"+strnum+"*    =    "+xmd5+"\n"
    f.write(nummd5)
    num+=1
f.close

print("Done!")
