###################################
# Ubuntu 16.04. install base utils 
###################################

# add repo
add-apt-repository ppa:jonathonf/python-3.6 -y  								# python3.6
add-apt-repository ppa:git-core/ppa -y											# git
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  	# docker
apt-key fingerprint 0EBFCD88
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"


# update system
apt update -qq && apt upgrade -y

# install base utils
apt install -y nano tree curl man wget net-tools traceroute

# install dev utils
apt install -y python3.6 git python3-pip postgresql-client

# install docker: https://docs.docker.com/engine/installation/linux/ubuntu/
apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

apt install -y docker-ce

# add configuration
git config --global color.ui auto
git config --global credential.helper cache

# Clean up APT when done.
apt autoremove -y
apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
