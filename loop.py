# importing "array" for array operations 
import os

def get_files(): 
	# Set variables
	cwd = os.getcwd()
	workspace = cwd+'/shows/'

	print("which show are you working on?")
	showlist = os.listdir(workspace)
	print('\n'.join(map(str, showlist)))
	show = input()
	workspace = workspace+show+'/'

	print("which shot are you working on?")
	shotlist = os.listdir(workspace)
	print('\n'.join(map(str, shotlist)))
	shot = input()
	workspace = workspace+shot+'/'

	print("which sequence are you working on?")
	sequence = os.listdir(workspace)
	print('\n'.join(map(str, sequence)))
	sequence = input()
	workspace = workspace+sequence

	print(workspace)

get_files()

