from utils.color import HEADER
import sys;


PROJECT_NAME:str =  "DEFAULT"

def set_project(name):
	PROJECT_NAME = name

def debug(*args,**kwargs):
	print(f'[{HEADER(PROJECT_NAME)}]',*args,**kwargs)
