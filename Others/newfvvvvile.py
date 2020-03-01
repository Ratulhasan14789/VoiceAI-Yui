with open("Yui_data/RAM/pdatas2.py","r") as udatafile:
	udataread=udatafile.read()
	filedata = udataread.replace('\n\t','\n\t\t'))
with open("Yui_data/RAM/pdatas2.py", "w") as udatanewfile:
	udatanewfile.write(filedata)