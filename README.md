# Gkernel


prerequisits : 
- bootable usb drive with linux distribution you want to install
- place to store files on chromebook


to install linux on your chromebook you will need to update the firmware.
use the  firmware update tool from mrchromebox: https://mrchromebox.tech/#fwscript

there are 2 versions available: UEFI Firmware (Full ROM) and RW_LEGACY Firmware

the main differences are: 

| description |UEFI Firmware (Full ROM) |RW_LEGACY Firmware |
| ----------- | ----------- |  ----------- | 
|keep warrenty | ❌ |✔️|
|boot chrome os |❌|✔️|
|bios boot support |❌  |✔️ |
|boot without pressing keys |✔️ |❌ |
|uefi boot support |✔️ |❌ |
|needs write protect disabled |✔️ |❌ |
|updated ec firmware|✔️|❌|


  
### if you picked UEFI Firmware
you need to disable write protect, to do this remove the battery from the device and boot it from ac charger 

### if you picked RW_LEGACY Firmware
no need to disable write protect just follow the rest of the guide


### flash firmware
make sure you are on the stable branch of chros and you have backuped all your files\
you will need to enable developer mode and this WILL DELETE YOUR FILES,\
to enter developer mode:
 - press ctrl+d while pressing the powerbutton
 - press enter on the warning

the chromebook wil switch to developer mode
on the next boot it will show "OS verification is off." press ctrl d to boot to developer mode\
now you need to open a developer shell and flash te firmware:
- open a developer shell login as guest
- and press ctrl-alt-t in the cros terminal type: shell

download and run the mrchromebox firmware script copy and paste and run: 
```
cd; curl -LO mrchromebox.tech/firmware-util.sh
sudo install -Dt /usr/local/bin -m 755 firmware-util.sh
sudo firmware-util.sh
```

now follow the https://mrchromebox.tech/#fwscript information for your desired firmware


### if you picked UEFI Firmware

boot your chrome book from usb just like a regular computer
and add the repositiory to install the kernel and touchpad/ audio fixes

# Linux distributions such as Ubuntu, Mint etc.

## 1. Install our official public software signing key
```
wget -O- https://deb.h-bomb.nl/grepo-archive-keyring.gpg | sudo tee -a /usr/share/keyrings/grepo-archive-keyring.gpg  > /dev/null
```
## 2. Add our repository to your list of repositories
```
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/grepo-archive-keyring.gpg ] https://deb.h-bomb.nl/amd64/ jammy main' |\
  sudo tee -a /etc/apt/sources.list.d/grepo-jammy.list
```
## 3. Update your package database and install the gkernel and touchpad/audio fixes
```
sudo apt update && sudo apt install  acer-chromebook-fixes linux-image-6.1.0atom linux-headers-6.1.0atom linux-libc-dev
```
