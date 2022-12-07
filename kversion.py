import os 
import shutil

image_sourcefiles= ["./linux/debian/linux-image/DEBIAN/control", "./linux-image-control"]
headers_sourcefiles=["./linux/debian/linux-headers/DEBIAN/control","./linux-headers-control"]
libc_sourcefiles=["./linux/debian/linux-libc-dev/DEBIAN/control","./linux-libc-dev-control"]


def copyallconfig():
	shutil.copyfile(image_sourcefiles[0], image_sourcefiles[1])
	shutil.copyfile(headers_sourcefiles[0], headers_sourcefiles[1])
	shutil.copyfile(libc_sourcefiles[0], libc_sourcefiles[1])


optionsindex=0
with open(image_sourcefiles[0], encoding = 'utf-8') as f:
	values=f.readlines()
	for item in values:
		if "Version:" in item:
			sourceversion=item.split(":")[-1].split('-')[0]
			sourcebuildversion=item.split(":")[-1].split('-')[-1]

if os.path.exists(image_sourcefiles[1]) and os.path.exists(headers_sourcefiles[1]) and os.path.exists(libc_sourcefiles[1]):
	#check version of kernel image if they dont match rest should be renewed too
	with open(image_sourcefiles[1], encoding = 'utf-8') as f:
		values=f.readlines()     
		for item in values:
			if "Version:" in item:
				ourversion=item.split(":")[-1].split('-')[0]
				ourbuildversion=item.split(":")[-1].split('-')[-1]

	if ourversion == sourceversion :
		
		if sourcebuildversion != ourbuildversion:
			print('good to copy')
		else:
			print('files build versions are the same')
		
	else:
		print("different main versions creating new control file in repo")
		copyallconfig()
else:
	print("no control files found creating new control files in repo")
	copyallconfig()

	
