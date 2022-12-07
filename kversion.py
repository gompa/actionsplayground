import os 
import shutil
import sys

githubworkspace=os.getenv('GITHUB_WORKSPACE')
print(githubworkspace)
repoversionfile="{githubworkspace}/version".format(githubworkspace=githubworkspace)
sourcedebversionfile="{githubworkspace}/linux/.version".format(githubworkspace=githubworkspace)
kernelrevisionfile="{githubworkspace}/linux/Makefile".format(githubworkspace=githubworkspace)

# sourcedebversionfile="../mainline-kernel/.version"
# kernelrevisionfile="../mainline-kernel/Makefile"


# copy function for after build to sync repo and source versions
if len(sys.argv) > 1:
	print(sys.argv[1])
	if sys.argv[1]=='cp':

		with open(sourcedebversionfile) as f:
			values=f.readlines()
			sourcebuildversion=values[0].strip('\n')
			# repokernelrevision=values[1].strip('\n')

		with open(kernelrevisionfile) as krevfile:
			config={}
			while len(config) < 6:

				line=krevfile.readline().strip('\n')
				if "=" in line:
					key=line.split('=')[0].replace(' ','')
					value=line.split('=')[1].replace(' ','')
					config[key]=value
				
		kernelrevisionromsource='{}.{}.{}{}'.format(config['VERSION'],config["PATCHLEVEL"],config['SUBLEVEL'],config["EXTRAVERSION"])	
		with open(repoversionfile,'w') as repoversion:
			repoversion.write('{}\n{}'.format(sourcebuildversion,kernelrevisionromsource))
		with open(repoversionfile,'r') as repoversionfile:				
			print('current repo version{}'.format(repoversionfile.readlines()))
else:

#default function checking and setting up source versions and repo versions
	with open(repoversionfile) as f:
		values=f.readlines()
		repobuildversion=values[0].strip('\n')
		repokernelrevision=values[1].strip('\n')

	with open(kernelrevisionfile) as krevfile:
		config={}
		while len(config) < 6:

			line=krevfile.readline().strip('\n')
			if "=" in line:
				key=line.split('=')[0].replace(' ','')
				value=line.split('=')[1].replace(' ','')
				config[key]=value
			
	kernelrevisionromsource='{}.{}.{}{}'.format(config['VERSION'],config["PATCHLEVEL"],config['SUBLEVEL'],config["EXTRAVERSION"])
	if repokernelrevision == kernelrevisionromsource:
		with open(sourcedebversionfile,'w') as kversion:
			kversion.write(repobuildversion)
		print("SAME, copying debversion")
	else:
		with open(repoversionfile,'w') as repoversion:
			repoversion.write('{}\n{}'.format('0',kernelrevisionromsource))	
		print('new kernel, set debversion to 0')

