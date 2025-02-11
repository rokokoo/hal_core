#!/bin/bash

# Give file permissions
chmod +x /opt/hal-core/runtest
chmod +x /opt/hal-core/src/clean
chmod +x /opt/hal-core/src/make
chmod +x /opt/hal-core/src/configure

# Compile hal-core
cd /opt/hal-core/src/
./configure --disable-gtk --with-realtime=uspace
./make && sudo make setuid


# Compile test component: 
chmod +x /opt/hal-core/src/hal/components/test/make
chmod +x /opt/hal-core/src/hal/components/test/runtest
cd /opt/hal-core/src/hal/components/test/ && ./make

# Compile ethercat component: 
chmod +x /opt/hal-core/src/hal/components/ethercat/make 
chmod +x /opt/hal-core/src/hal/components/ethercat/runtest
cd /opt/hal-core/src/hal/components/ethercat && ./make

# Compile threads component: 
chmod +x /opt/hal-core/src/hal/components/threads/make 
chmod +x /opt/hal-core/src/hal/components/threads/runtest
cd /opt/hal-core/src/hal/components/threads/ && ./make

# Compile dofs component: 
# To be reviewed compiling Rpi4.
# chmod +x /opt/hal-core/src/hal/components/dofs/make
# cd /opt/hal-core/src/hal/components/dofs/ && ./make

# Remove the actual halcmd that came with the image
sudo rm /usr/bin/halcmd

# Make a symbolic from new halcmd link for system wide usage
ln -s /opt/hal-core/bin/halcmd /usr/bin/halcmd
