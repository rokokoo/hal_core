
Hal_core is a lightweight hal environment.
The installed size is approx 6.8Mib

A hal environment can be used as platform to run realtime applications like:

	motion controllers 
	robots
	cnc-machines 
	parport, ethercat applications
	research and development 
	scientific projects

Packages needed for the installation (at the bottom):

To install:

	Install hal-core:
	$ git clone https://github.com/jjrbfi/hal-core.git /opt/hal-core
	$ sudo chown -R $USER:$USER /opt
	$ /opt/hal-core/./make
	$ sudo chown -R $USER:$USER /opt/hal-core
	
Before run:
Modify config/hal.yaml file with your Hardware configuration and then run hal_config.py to create our .xml

To run:

	$ /opt/hal-core/./runtest

https://user-images.githubusercontent.com/44880102/129791198-ab705999-23ca-4004-a5f5-f0bd3357b47e.mp4
