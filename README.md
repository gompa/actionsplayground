# Gkernel


mainline kernel for the bobba chromebooks


# Linux distributions such as Ubuntu, Mint etc.

# 1. Install our official public software signing key
wget -O- https://deb.h-bomb.nl/grepo-archive-keyring.gpg 
cat grepo-archive-keyring.gpg  | sudo tee -a /usr/share/keyrings/grepo-archive-keyring.gpg  > /dev/null

# 2. Add our repository to your list of repositories
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/grepo-archive-keyring.gpg ] https://deb.h-bomb.nl/amd64/ jammy main' |\
  sudo tee -a /etc/apt/sources.list.d/grepo-jammy.list

# 3. Update your package database and install signal
sudo apt update && sudo apt install linux-image-6.1.0-rc8atom linux-headers-6.1.0-rc8atom linux-libc-dev
