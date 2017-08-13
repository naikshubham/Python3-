'''Code to replace a directory if it exists '''



import os, sys,shutil
from pathlib import Path

my_dir='/home/coder/Arpan'
if not os.path.exists(my_dir):
	os.mkdir(my_dir)
	print("Directory Created")
else:
	shutil.rmtree(my_dir)
	os.mkdir(my_dir)
	print("Directory replaced");
