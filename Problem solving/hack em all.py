
from os import listdir, getcwd
print(getcwd())
print(listdir('/'))

import shutil
from os.path import join, basename, isdir
from os import listdir
def copytree(src, dst, symlinks=False, ignore=None):
	for item in listdir(src):
		s = join(src, item)
		d = join(dst, item)
		if isdir(s):
			try:
				shutil.copytree(s, d, symlinks, ignore)
			except:
				pass
		else:
			try:
				shutil.copy2(s, d)
			except: pass
		print(d)

#copytree('/data/user/0/ru.iiec.pydroid3/files/','/storage/emulated/0/MEGA/MEGA Downloads/PydroidRIP/')
print(00)