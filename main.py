import os
import subprocess


def check(file_path):
	''' Checks if the file is a homebrew symlink'''
	output = subprocess.run([f'ls -la {file_path}'],capture_output=True, text=True, shell=True)

	key = 'Cellar'
	return(key in output.stdout)


def get_all_brew_symlinks(path):
	''' Returns a list of all Homebrew symlinks'''
	list_of_files = []
	all_files = os.listdir(path)
	for file in all_files:
		file_path = f'{path}/{file}'
		if not os.path.isdir(file_path):
			if check(file_path):
				list_of_files.append(file)

	return list_of_files
