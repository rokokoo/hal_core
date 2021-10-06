#!/usr/bin/env python3

import yaml

hal_config = "hal.yaml"

with open(hal_config, "r") as stream:
	try:
		data = yaml.safe_load(stream)
		xml_o = '<masters>\n'
		xml_o += '\t<master idx="{masteridx}" appTimePeriod="{apptimeperiod}" refClockSyncCycles="{refclocksynccycles}">\n'
		
		for count,name in enumerate(data['ETHERCAT']['SLAVES']):
			xml_o += '\t\t<slave idx="{count}" type="{name}" />\n'.format(count=count, name=name)

		xml_o += '\t</master>\n</masters>'
		xml_o = xml_o.format(masteridx=data['ETHERCAT']['MASTERIDX'], apptimeperiod=data['ETHERCAT']['APPTIMEPERIOD'], refclocksynccycles=data['ETHERCAT']['REFCLOCKSYNCCYCLES'])
		print(xml_o)
		f = open('hal.xml', 'w')
		f.write(xml_o)
		f.close()
	except yaml.YAMLError as exc:
		print(exc)