import re
a=open('non_vowels.txt','w')
with open('english3.txt','r') as x:
	for i in x.readlines():
		if re.match('^[^aeiou]+$',i):
			print(i)
			a.write(i+'\n')
a.close()