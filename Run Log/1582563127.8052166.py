# Earlier it was named "hackrun" because it is full of hacky code.
# Some dudes didn't get it tho, so we had to rename it. Hopefully they are happy now.
import os
import sys
from time import time
is_pydroid_2 = sys.version_info.major == 2
mainpyfile = sys.argv[1]
del sys.argv[0]
fakepyfile = os.getenv("ANDROID_ORIGFNAME",mainpyfile)
sys.path[0] = os.path.dirname(fakepyfile)
sys.argv[0] = fakepyfile

def start(fakepyfile,mainpyfile,time):
	if(is_pydroid_2):
		import __main__
		tmp=__main__.__builtins__
		__main__.__dict__.clear()
		__main__.__dict__.update({"__name__"    : "__main__",
					  "__file__"    : fakepyfile,
					  "__builtins__": tmp,
					 })
		execfile(mainpyfile,  __main__.__dict__)
	else:
		import __main__
		
		start69up=time
		tmp=__main__.__builtins__
		__main__.__dict__.clear()
		__main__.__dict__.update({"__name__"    : "__main__",
					  "__file__"    : fakepyfile,
					  "__builtins__": tmp,
					 })
		with open('/storage/emulated/0/MEGA/MEGA Downloads/Python/Run Log/'+str(time)+".py",'w') as f:
			f.write(open(mainpyfile).read())
			
		exec(open(mainpyfile).read(),  __main__.__dict__)
		print('\n\n[Runtime: ', time()-start69up,'s]')
start(fakepyfile,mainpyfile,time())
