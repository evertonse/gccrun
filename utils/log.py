from color import bcolors
import sys;


__filename__,_ =  __file__[__file__.rindex('\\')+1:].rsplit('.',1)

def debug(*args,**kwargs):
	print(f'[{bcolors.HEADER(__filename__)}]',*args,**kwargs)