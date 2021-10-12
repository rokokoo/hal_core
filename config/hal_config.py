#!/usr/bin/env python3

import yaml, collections

def parseModParam(modParam):
	xml_o = ""
	for param in modParam:
		parName = list(param.keys())[0]
		parVal = param[parName]
		xml_o += '\n\t\t\t<modParam name="{}" value="{}" />'.format(parName,parVal)

	return xml_o

def parseTerminal(idx, terminal):
	xml_o = '\n\t\t<slave' 
	if isinstance(terminal,dict):
		term_type = list(terminal.keys())[0]
		xml_o += ' idx="{}" type="{}"'.format(idx,term_type)

		term = terminal[term_type]

		for i in term:
			keys = i.keys()
			# print(keys)
			if 'name' in keys:
				name = i['name'] 
				xml_o += ' name="{}"'.format(i['name'])
			
			if 'modParam' in keys:
				xml_o += parseModParam(i['modParam'])
			else:
				xml_o += '>'
		xml_o += '\n\t\t</slave>'
	else:
		xml_o += ' idx="{}" type="{}" />'.format(idx,terminal)

	return xml_o

hal_config = "hal.yaml"

with open(hal_config, "r") as stream:
	try:
		data = yaml.safe_load(stream)

		xml_o = '<masters>\n'
		xml_o += '\t<master idx="{masteridx}" appTimePeriod="{apptimeperiod}" refClockSyncCycles="{refclocksynccycles}">'
		
		for count,terminal in enumerate(data['ETHERCAT']['SLAVES']):
			xml_o += parseTerminal(count, terminal)

		xml_o += '\n\t</master>\n</masters>'
		xml_o = xml_o.format(masteridx=data['ETHERCAT']['MASTERIDX'], apptimeperiod=data['ETHERCAT']['APPTIMEPERIOD'], refclocksynccycles=data['ETHERCAT']['REFCLOCKSYNCCYCLES'])
		# print(xml_o)
		f = open('hal.xml', 'w')
		f.write(xml_o)
		f.close()
	except yaml.YAMLError as exc:
		print(exc)