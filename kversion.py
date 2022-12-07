import os 
import shutil

githubworkspace=os.getenv('GITHUB_WORKSPACE')
print(githubworkspace)

repoversionfile="version"
sourcedebversionfile="{githubworkspace}/linux/.version".format(githubworkspace=githubworkspace)
kernelrevisionfile="{githubworkspace}/linux/Makefile".format(githubworkspace=githubworkspace)
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
		
kernelversionfromsource='{}.{}.{}{}'.format(config['VERSION'],config["PATCHLEVEL"],config['SUBLEVEL'],config["EXTRAVERSION"])
if repokernelrevision == kernelversionfromsource:
	with open(sourcedebversionfile,'w') as kversion:
		kversion.write(repobuildversion)
	print("SAME, copying debversion")
else:
	print('new kernel no version file needed')
