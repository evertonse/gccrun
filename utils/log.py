from os.path import basename,splitext
class bcolors:
	HEADER 	 = '\033[95m'
	OKBLUE 	 = '\033[94m'
	OKCYAN 	 = '\033[96m'
	OKGREEN  = '\033[92m'
	WARNING  = '\033[93m'
	FAIL 	 = '\033[91m'
	ENDC 	 = '\033[0m'
	BOLD 	 = '\033[1m'
	UNDERLINE= '\033[4m'

import inspect

THIS_PACKAGE_NAME:str =  "DEFAULT"

def RED(msg:str) -> str:
	return f"{bcolors.FAIL}{msg}{bcolors.ENDC}"

def GREEN(msg:str) -> str:
	return f"{bcolors.OKGREEN}{msg}{bcolors.ENDC}"

def BLUE(msg:str) -> str:
	return f"{bcolors.OKCYAN}{msg}{bcolors.ENDC}"

def HEADER(msg:str) -> str:
	return f"{bcolors.HEADER}{msg}{bcolors.ENDC}"


def set_project(name):
	PROJECT_NAME = name

def debug(*args,**kwargs):
	filename = splitext(basename(inspect.stack()[1].filename))[0] 
	print(f'[{HEADER(filename)}]',*args,**kwargs)