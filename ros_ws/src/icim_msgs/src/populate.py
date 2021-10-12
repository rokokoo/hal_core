#!/usr/bin/env python3
from yaml.loader import SafeLoader
import rospy, icim_msgs.msg, time, argparse
from std_msgs.msg import String

# def talker():
#     pub = rospy.Publisher('chatter', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(100) # 10000hz
#     while not rospy.is_shutdown():
#         information = subprocess.run(['halcmd','getp','lcec.0.7.enc-0-pos'], capture_output=True).stdout.decode('utf-8').strip() 
#         hello_str = "hello world %s" % rospy.get_time()
#         rospy.loginfo(information)
#         pub.publish(information)
#         rate.sleep()

class HALcmdPopulator():
	def __init__(self, param_name) -> None:
		params = rospy.get_param(param_name)

		self.publishers = []
		self.mod = getattr(__import__('icim_msgs'),'msg')

		# Going through the YAML slaves
		for count, terminal in enumerate(params['slaves']):
			if isinstance(terminal, dict):
				term_type = list(terminal.keys())[0]
				# print(term_type)
				name = None
				for i in terminal[term_type]:
					keys = i.keys()
					if 'name' in keys:
						name = i['name']

				if name is None:
					self.topic_name = '/icim/terminal_{:02d}/{}'.format(count,term_type)
				else:
					self.topic_name = '/icim/terminal_{:02d}/{}'.format(count,name)

				msg_type = getattr(self.mod,term_type)

			else:
				self.topic_name = '/icim/terminal_{:02d}/{}'.format(count, terminal)
				msg_type = getattr(self.mod, terminal)
				
			publisher = rospy.Publisher(self.topic_name, msg_type, queue_size=1)
			self.publishers.append(publisher)
			
		

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	parser.add_argument('-param', default='hal')

	args,_ = parser.parse_known_args()

	rospy.init_node('icim_populator')

	if rospy.has_param(args.param):
		populator = HALcmdPopulator(args.param)

		r = rospy.Rate(1)
		while not rospy.is_shutdown():
			r.sleep()
	else:
		rospy.logerr('Param {param} was not set!'.format(param=args.hal))
