import sys
from dataclasses import dataclass
import os
import subprocess
import tomllib as toml
import pathlib
from collections import defaultdict


from utils.log import debug,set_project,RED,BLUE,GREEN,HEADER
from utils.package_test import package_setup



__filename__,_ =  __file__[__file__.rindex('\\')+1:].rsplit('.',1)

#>>========================================================================================================
#>>=============================================CONFIG PROEJCT=============================================
# WARNING:
# 	require either tomllib installed or python 3.11 (tomllib became part of the standard library for python 3.11)
# PLEASE:
# 	Create a toml files as your project config
# 	Define **ALL** variables listed in the class Project bellow, don't need to be in order
# 	Then populate with the desired values using the type indicated below
@dataclass
class Project():
	name :str 
	
	compiler :str		# can optionally use full path
	language :str  	# ignored for now
	version  :str
	binpath 	 :str # directory for binaries, if
	#-O
	optimize :str
	srcfiles 		:list[str]
	# -D
	defines 		:list[str]
	# -I
	includedirs	:list[str]
	# -L
	libdirs 		:list[str]
	# -l
	libfiles 		:list[str]
	#-W
	warnings 		:list[str]
#<<=========================================================================================================
#<<=========================================================================================================

	def __init__(self,toml_dict) -> None:
		self.__dict__ = toml_dict
		self.binpath = pathlib.Path(pathlib.PurePath('./'+ toml_dict['binpath']))
		self.binpath.mkdir(parents=True,exist_ok=True)
		self.add_src_files()

	# // TODO(Everton): "ADD Regex to this"
	def add_src_files(self):
		for srcfile in list(self.srcfiles):
			if srcfile.endswith("**"):
				
				srcdir = srcfile[:len(srcfile)-2]
				for file in os.listdir(srcdir):
					if file.endswith(".cpp") or file.endswith(".c"):
						self.srcfiles.append(os.path.join(srcdir, file))
				
				self.srcfiles.remove(srcfile)

	def executable_path(self):
		return str(pathlib.PurePath(self.binpath,self.name))

# cdir = os.getcwd() # it will return current working directory
# print("Previous_dir",cdir)

# # Previous_dir C:\Users\..\Desktop\python
# os.chdir('./..') #chdir used for change direcotry
# print("Current_dir",cdir)





def create_cmd(
	compiler:str,
	project:Project) -> str:
	
	version  :str  = project.version.lower() if project.version else ""
	optimized :bool = True if project.optimize == "on" else False

	version_flag  :str  = f'-std={version}' if version != "" else ""
	
	cmd = f'{compiler} {version_flag}'

	for file in project.srcfiles:
		cmd += f' ./{file} '
		

	for folder in project.includedirs:
		cmd += f' -I{folder} '

	for folder in project.libdirs:
		cmd += f' -L{folder} '

	for warning in project.warnings:
		cmd += f' -W{warning} '
	
	for define in project.defines:
		cmd += f' -D{define} '

	for file in project.libfiles:
		cmd += f' -l{file} '
		
	
	cmd += (" -O3 " if optimized else "-O0 ")
	
	cmd += f'-o{project.executable_path()}'

	return cmd

def __main__():

	default_project_path = 'CyberXEngine.toml'
	project_path = sys.argv[1] if len(sys.argv) > 1 else default_project_path
	
	with open(project_path, "rb") as f:
		data	 	= defaultdict(lambda:"",toml.load(f))
		project = Project(data)
	
	config = {
		"compiler" : project.compiler if project is not None else 'g++', 
	}

	cmd = create_cmd(
		compiler=config['compiler'],
		project =project
	)
	
	debug(f"INFO: Building project from file : {BLUE(project_path)}\n")
	debug(f"INFO: Command Generated: {cmd}\n")
	debug(f"INFO: Running project from file : {BLUE(project_path)}\n")
	
	code = subprocess.run(cmd)
	
	if code.returncode == 0:
		debug(f'INFO: {GREEN("Compilation Succeded")} return code was zero, usually means success')
		subprocess.run(project.executable_path())
	else:
		debug(f'ERROR: {RED("Compilation Failed")} return code was {RED("non-zero")}, usually means bad things')

if __name__ == '__main__':
	__main__()
