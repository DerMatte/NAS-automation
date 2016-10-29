import os
import os.path
folder_path = "wirdsortiert"
while 1:
	cwd = os.getcwd()
	print cwd
	/Users/Matte
	images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
