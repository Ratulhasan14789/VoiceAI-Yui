import random
serial=[1,2,3,4,5,6,7,8]
serial2=serial
ink=[]
key_list="abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTWXYZ1234567890+-*/.,\\<>?;':\"[]{}|_=`~!@#$%^&() "
print(key_list)
def key_gen():
	global serial2,serial,ink
	for c in key_list:
		serial2 = [1,2,3,4,5,6,7,8]
		while len(serial2)>0:
			a=random.choice(serial2)
			ink.append(a)
			serial2.remove(a)
			print(ink,serial2)

		print(ink,serial2)
		with open("Yui_data/ROM/key_gen.txt", "a") as inject:
			inject.write(c+' = '+str(ink)+'\n')
		alone=str(ink)
		alone=alone[1:len(alone)-1]
		with open("RCrypt_easy.py", "a") as inject:
			inject.write('elif key_c=="'+c+'": denlock1(a, '+alone+')\n')

		print(c+' Done',end='\r')
		ink=[]

	print('All Done!')
key_gen()
