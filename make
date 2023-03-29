#!/bin/bash

# Give file permissions
chmod +x /opt/hal-core/runtest
chmod +x /opt/hal-core/src/clean
chmod +x /opt/hal-core/src/make
chmod +x /opt/hal-core/src/configure
chmod +x /opt/hal-core/scripts/halrun
chmod +x /opt/hal-core/scripts/realtime

# Compile cROS and copy shared library
if [ -f /opt/hal-core/src/hal/components/cros/build/libcros.so ]; then
	echo "Exist!"
else
  mkdir /opt/hal-core/src/hal/components/cros/build
  cd /opt/hal-core/src/hal/components/cros/build && cmake ..
  cd /opt/hal-core/src/hal/components/cros/build/ && make
  ln -s /opt/hal-core/src/hal/components/cros/build/libcros.so /opt/hal-core/lib/
  ln -s /opt/hal-core/src/hal/components/cros/samples/rosdb/ /opt/hal-core/
  ln -s /opt/hal-core/src/hal/components/cros/include/ /opt/hal-core/src/cros
fi

# Compile hal-core
cd /opt/hal-core/src/
./configure --disable-gtk --with-realtime=uspace
./make && sudo make setuid

# Set user able to insert kernel modules
chown 777 -R /opt/hal-core/bin/rtapi_app
chown 777 -R /opt/hal-core/bin/module_helper
chmod 777 /opt/hal-core/bin/rtapi_app
chmod 777 /opt/hal-core/bin/module_helper 

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
