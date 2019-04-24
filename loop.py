import os
from sys import platform

# Get operating system
def get_os():
	if platform == "linux" or platform == "linux2":
	    # linux
	    get_workspace()
	elif platform == "darwin":
	    # OS X
	    get_workspace()
	elif platform == "win32":
	    # Windows...
	    get_workspace()

# Get working directory
def get_workspace(): 
	# Create the working directory by prompting the user for folders in the directory list
	cwd = os.getcwd()
	workspace = cwd+'/shows/'

	
	directory = {
		"show" : None,
		"shot" : None,
		"sequence" : None
	}

	for key in directory:
		print("Which "+key+"?")
		item = os.listdir(workspace)
		print('\n'.join(map(str, item)))
		directory[key] = input()
		workspace = workspace+directory[key]+'/'

	print(workspace)

get_os()

