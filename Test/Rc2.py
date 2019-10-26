#Python3 program to Convert list of
# strings to space separated string
def Joiner(list):
	return ' '.join(list)
# Driver code


def reverser(x):
	x[::-1]
	return x

# Python code to convert string to list
def spliter(string):
	li = list(string.split(' '))
	return li


# Text splitter by LENTH
#inputs = input("This is the text which is decrypted!")
def len_split(x):
	global split_li
	split_li = []
	length = 8
	for i in range(len(x))[::length]:
		split_li.append(x[i:i+length])
	return split_li

def c_split(s):
	for i in s:
		abc=[]
		for c in i:
			abc.append(c)
		s[s.index(i)] = abc
	return s

def add_ser(li):
	for i in li:
		n=1
		for c in i:
			i[i.index(c)]=[c,n]
			n+=1
	return li

def denlock1(abc,key,bit=0):
	print(key)
	if bit==1:
		n=1
		codec=[]
		while n<9:
			xx=key.index(n)+1
			codec.append(xx)
			n+=1
	else:
		codec=key
	print(codec)
	print(abc)
	res = [list for x in codec for list in abc if list[1] == x]
	print("==",key,"==")
	print(res)
	out=[]
	for i in res:
		out.append([i[0],res.index(i)+1])
		print(out)
	return out

def denlock2(text,key_c,bit=0):
	if key_c=="a": seq= [8, 3, 1, 6, 4, 7, 2, 5]
	elif key_c=="b": seq= [3, 7, 1, 5, 8, 6, 2, 4]
	elif key_c=="c": seq= [7, 6, 3, 5, 1, 4, 2, 8]
	elif key_c=="d": seq= [3, 2, 4, 5, 6, 8, 7, 1]
	elif key_c=="e": seq= [1, 5, 3, 7, 6, 4, 8, 2]
	elif key_c=="f": seq= [3, 1, 8, 5, 2, 7, 4, 6]
	elif key_c=="g": seq= [8, 2, 1, 4, 7, 3, 5, 6]
	elif key_c=="h": seq= [8, 1, 6, 7, 4, 3, 5, 2]
	elif key_c=="i": seq= [4, 5, 6, 7, 2, 1, 8, 3]
	elif key_c=="j": seq= [6, 5, 8, 3, 7, 4, 2, 1]
	elif key_c=="k": seq= [8, 2, 4, 5, 6, 7, 3, 1]
	elif key_c=="l": seq= [8, 6, 7, 1, 3, 2, 5, 4]
	elif key_c=="m": seq= [4, 1, 3, 7, 6, 5, 8, 2]
	elif key_c=="n": seq= [1, 8, 3, 2, 4, 7, 5, 6]
	elif key_c=="o": seq= [6, 7, 4, 8, 5, 1, 3, 2]
	elif key_c=="p": seq= [4, 7, 3, 6, 8, 5, 2, 1]
	elif key_c=="q": seq= [7, 1, 2, 3, 4, 5, 6, 8]
	elif key_c=="r": seq= [4, 3, 8, 2, 5, 6, 7, 1]
	elif key_c=="s": seq= [8, 4, 1, 3, 2, 7, 6, 5]
	elif key_c=="t": seq= [2, 8, 1, 7, 4, 3, 5, 6]
	elif key_c=="w": seq= [3, 5, 6, 7, 4, 8, 2, 1]
	elif key_c=="x": seq= [5, 6, 1, 3, 2, 8, 4, 7]
	elif key_c=="y": seq= [8, 4, 2, 3, 5, 6, 7, 1]
	elif key_c=="z": seq= [3, 7, 2, 8, 5, 4, 6, 1]
	elif key_c=="A": seq= [5, 1, 7, 3, 8, 4, 6, 2]
	elif key_c=="B": seq= [6, 5, 4, 2, 7, 3, 1, 8]
	elif key_c=="C": seq= [7, 2, 3, 8, 4, 6, 5, 1]
	elif key_c=="D": seq= [2, 3, 7, 1, 6, 4, 5, 8]
	elif key_c=="E": seq= [7, 6, 5, 3, 2, 4, 1, 8]
	elif key_c=="F": seq= [8, 1, 2, 5, 4, 6, 3, 7]
	elif key_c=="G": seq= [2, 5, 7, 6, 1, 8, 4, 3]
	elif key_c=="H": seq= [8, 3, 2, 5, 4, 6, 7, 1]
	elif key_c=="I": seq= [6, 2, 8, 7, 1, 3, 4, 5]
	elif key_c=="J": seq= [2, 1, 7, 8, 4, 5, 3, 6]
	elif key_c=="K": seq= [7, 8, 4, 3, 5, 1, 6, 2]
	elif key_c=="L": seq= [8, 2, 4, 3, 5, 6, 7, 1]
	elif key_c=="M": seq= [1, 2, 8, 7, 5, 6, 3, 4]
	elif key_c=="N": seq= [1, 6, 5, 8, 3, 4, 2, 7]
	elif key_c=="O": seq= [2, 5, 3, 8, 1, 7, 6, 4]
	elif key_c=="P": seq= [3, 1, 7, 2, 4, 5, 8, 6]
	elif key_c=="Q": seq= [7, 1, 5, 8, 6, 2, 3, 4]
	elif key_c=="R": seq= [8, 6, 3, 5, 2, 4, 7, 1]
	elif key_c=="S": seq= [7, 3, 2, 4, 5, 1, 8, 6]
	elif key_c=="T": seq= [4, 6, 7, 2, 5, 8, 3, 1]
	elif key_c=="W": seq= [1, 8, 5, 3, 6, 7, 2, 4]
	elif key_c=="X": seq= [4, 6, 1, 2, 7, 8, 3, 5]
	elif key_c=="Y": seq= [1, 2, 4, 8, 5, 7, 6, 3]
	elif key_c=="Z": seq= [1, 4, 7, 3, 8, 5, 2, 6]
	elif key_c=="1": seq= [2, 5, 7, 4, 6, 1, 8, 3]
	elif key_c=="2": seq= [7, 5, 8, 3, 6, 2, 4, 1]
	elif key_c=="3": seq= [4,3,1,2,8,6,7,5]
	elif key_c=="4": seq= [2,5,8,6,3,7,4,1]
	elif key_c=="5": seq= [4, 8, 5, 2, 3, 7, 1, 6]
	elif key_c=="6": seq= [1, 4, 6, 8, 7, 3, 5, 2]
	elif key_c=="7": seq= [2, 5, 3, 6, 1, 4, 7, 8]
	elif key_c=="8": seq= [1, 7, 4, 6, 3, 5, 2, 8]
	elif key_c=="9": seq= [6, 2, 8, 5, 1, 7, 4, 3]
	elif key_c=="0": seq= [3, 2, 7, 5, 1, 4, 6, 8]
	elif key_c=="+": seq= [3, 8, 7, 6, 4, 5, 2, 1]
	elif key_c=="-": seq= [6, 7, 5, 2, 8, 3, 1, 4]
	elif key_c=="*": seq= [3, 1, 2, 7, 5, 8, 4, 6]
	elif key_c=="/": seq= [2, 1, 8, 7, 6, 4, 3, 5]
	elif key_c==".": seq= [8, 6, 7, 2, 5, 1, 4, 3]
	elif key_c==",": seq= [2, 3, 8, 4, 6, 1, 7, 5]
	elif key_c=="\\": seq= [3, 5, 6, 1, 2, 7, 8, 4]
	elif key_c=="<": seq= [1, 4, 6, 5, 2, 7, 3, 8]
	elif key_c==">": seq= [4, 5, 3, 1, 6, 2, 7, 8]
	elif key_c=="?": seq= [4, 3, 2, 5, 7, 1, 8, 6]
	elif key_c==";": seq= [4, 5, 6, 8, 2, 1, 3, 7]
	elif key_c=="'": seq= [2, 1, 8, 5, 3, 7, 6, 4]
	elif key_c==":": seq= [1, 7, 4, 8, 5, 2, 6, 3]
	elif key_c=='"': seq= [1, 6, 7, 3, 8, 4, 2, 5]
	elif key_c=="[": seq= [3, 2, 8, 5, 1, 6, 7, 4]
	elif key_c=="]": seq= [6, 1, 8, 4, 2, 7, 3, 5]
	elif key_c=="{": seq= [4, 2, 1, 7, 6, 8, 3, 5]
	elif key_c=="}": seq= [5, 7, 8, 1, 3, 2, 4, 6]
	elif key_c=="|": seq= [7, 6, 4, 2, 3, 1, 8, 5]
	elif key_c=="_": seq= [1, 3, 4, 7, 8, 6, 5, 2]
	elif key_c=="=": seq= [4, 2, 7, 8, 3, 6, 5, 1]
	elif key_c=="`": seq= [2, 7, 8, 4, 6, 3, 1, 5]
	elif key_c=="~": seq= [7, 3, 2, 8, 1, 4, 5, 6]
	elif key_c=="!": seq= [6, 7, 8, 4, 3, 5, 2, 1]
	elif key_c=="@": seq= [3, 2, 5, 7, 1, 4, 8, 6]
	elif key_c=="#": seq= [8, 4, 1, 2, 5, 6, 7, 3]
	elif key_c=="$": seq= [6, 1, 3, 5, 7, 2, 8, 4]
	elif key_c=="%": seq= [6, 1, 5, 7, 2, 4, 8, 3]
	elif key_c=="^": seq= [7, 8, 3, 6, 2, 5, 4, 1]
	elif key_c=="&": seq= [5, 8, 3, 4, 6, 1, 2, 7]
	elif key_c=="(": seq= [5, 6, 1, 4, 8, 7, 3, 2]
	elif key_c==")": seq= [1, 4, 6, 5, 2, 8, 3, 7]
	elif key_c==" ": seq= [2, 6, 7, 8, 3, 4, 5, 1]
	if bit==0:
		y=denlock1(text,seq,0)
	elif bit==1:
		y=denlock1(text,seq,1)
	return y


def encrypt(text,key):
	code1= add_ser(c_split(len_split(text)))
	for key_c in key:
		for i in code1:
			code1[code1.index(i)] = denlock2(i,key_c,0)
	output=''
	for list in code1:
		print(list)
		for tuple in list:
			output+=tuple[0]
	return output

def sortSecond(val):
    return val[1]

def decrypt(text,key):
	key=reverser(key)
	code1= add_ser(c_split(len_split(text)))
	for key_c in key:
		for i in code1:
			code1[code1.index(i)] = denlock2(i,key_c,1)
	output=''
	for list in code1:
		print(list)
		for tuple in list:
			output+=tuple[0]
	return output

light=encrypt('12345678','b')


print('\n\n========\n\n]')

dark=decrypt(light,'b')

print(light)


print(dark)

"""X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
Y = [4, 2, 3, 7, 5, 1, 6, 8, 9]

Z = [x for _,x in sorted(zip(Y,X))]
print(Z)"""
