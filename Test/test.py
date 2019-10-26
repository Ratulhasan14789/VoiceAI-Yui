import re
text="i live in {{dacca||dhaka}}"
if '||' in text:
	t1=text.split('||')
	for s in t1:
		a=re.search('{{',s)
		if a:
			t1[t1.index(s)]=s.replace('{{','')
		b=re.search('}}',s)
		if b:
			b=b.span()
			t1[t1.index(s)]=t1[t1.index(s)][b[1]:len(s)-1]
	text=''
	for s in t1: text+=s
print(text)
