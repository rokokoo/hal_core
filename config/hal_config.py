#!/usr/bin/env python3

import yaml

hal_config = "hal.yaml"

with open(hal_config, "r") as stream:
	try:
		data = yaml.safe_load(stream)
		xml_o = '<masters>\n'
		xml_o += '\t<master idx="{masteridx}" appTimePeriod="{apptimeperiod}" refClockSyncCycles="{refclocksynccycles}">\n'
		
		for count,type in enumerate(data['ETHERCAT']['SLAVES']):

			if isinstance(type,dict):
				terminal_type = list(type.keys())[0]
				terminal_name = type[terminal_type]['name']
				xml_o += '\t\t<slave idx="{count}" type="{type}" name="{name} />\n'.format(count=count,type=terminal_type,name=terminal_name)
			else:
				xml_o += '\t\t<slave idx="{count}" type="{type}" />\n'.format(count=count, type=type)

		xml_o += '\t</master>\n</masters>'
		xml_o = xml_o.format(masteridx=data['ETHERCAT']['MASTERIDX'], apptimeperiod=data['ETHERCAT']['APPTIMEPERIOD'], refclocksynccycles=data['ETHERCAT']['REFCLOCKSYNCCYCLES'])
		print(xml_o)
		f = open('hal.xml', 'w')
		# f.write(xml_o)
		f.close()
	except yaml.YAMLError as exc:
		print(exc)