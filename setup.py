import sys
import subprocess as sp
from utils.color import RED,GREEN, BLUE
from utils.log import debug 
import pkg_resources

PACKAGES_REQUIRED:list[str] = ['pathlib','tomllib']

def package_check(package:str):
	package_name = BLUE(package)
	try:
		dist = pkg_resources.get_distribution(package)
		debug(f"INFO: package {package_name} was found {GREEN('successfully')}")

	except pkg_resources.DistributionNotFound:
		debug(f"ERROR: package {package_name} was not found")
		debug(f"Would you like to install {package_name} ?. It's necessary to run properly")
		input(f"press crtl+c to quit, {RED('else')} it'll install it")
		sp.check_call([sys.executable, '-m', 'pip', 'install', package])

def setup():
	for package in PACKAGES_REQUIRED:
		package_check(package=package)