#from tika import parser

#raw = parser.from_file('sao pro vol 1.pdf')
#print(raw['content'])
loc='book/'
t=26.5
from os import listdir
import re
from threading import Thread
from os.path import isfile, join
#import collections
from time import sleep
import PyPDF2
def run(loc):
	pdf_file = open(loc,'rb')
	read_pdf = PyPDF2.PdfFileReader(pdf_file)
	number_of_pages = read_pdf.getNumPages()
	print(number_of_pages)
	a=''
	for i in range(number_of_pages):
		print(i/number_of_pages*100, end='\r')
		page = read_pdf.getPage(i)
		page_content = page.extractText()
		#print(page_content)
		a+=page_content
	pdf_file.close()
	return a
on = [loc+f for f in listdir(loc) if isfile(join(loc, f)) if f.endswith('.pdf')]
print(on)
for i in on:
	if isfile(i[:len(i)-4]+'.txt'):
		with open(i[:len(i)-4]+'.txt','r') as s:
			if s.read().endswith('==()=='):
				pass
			else:
				with open(i[:len(i)-4]+'.txt','w') as f:
					print(i[:len(i)-4]+'.txt')
					x=run(i)
					f.write(x)
					f.write('==()==')
	else:
		with open(i[:len(i)-4]+'.txt','w') as f:
			print(i[:len(i)-4]+'.txt')
			x=run(i)
			f.write(x)
			f.write('==()==')
