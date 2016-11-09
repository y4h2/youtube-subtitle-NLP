import pycaption

import re
import datetime 

"""
 extract the content between the time [mid_time - delta, mid_time + delta]
 input mid_time format: HH:MM:SS
 delta: minutes
"""
def extract_content(fname, mid_time, delta, m_s_switch='minute'):
	base_dir = 'resources/subtitles/'
	pattern = '(\d{2}:\d{2}:\d{2}).\d{3} --> (\d{2}:\d{2}:\d{2}).\d{3}'
	content_buffer = ''
	read_flag = False
	
	if m_s_switch == 'minute':
		start_time = datetime.datetime.strptime(mid_time, "%H:%M:%S") - datetime.timedelta(minutes = int(delta))
		end_time = datetime.datetime.strptime(mid_time, "%H:%M:%S") + datetime.timedelta(minutes = int(delta))
	elif m_s_switch == 'second':
		start_time = datetime.datetime.strptime(mid_time, "%H:%M:%S") - datetime.timedelta(seconds = int(delta))
		end_time = datetime.datetime.strptime(mid_time, "%H:%M:%S") + datetime.timedelta(seconds = int(delta))

	with open(base_dir + fname) as f:
		lines = f.readlines()

	# max_time = datetime.strptime('0:0:0', "%H:%M:%S")

	for line in lines:
		m = re.search(pattern, line)
		if m:
			[timestamp1, timestamp2] = m.groups()
			# max_time = timestamp2
			t1 = datetime.datetime.strptime(timestamp1, "%H:%M:%S")
			t2 = datetime.datetime.strptime(timestamp2, "%H:%M:%S")

			# t2 < start_time: not read
			if (t2 < start_time):
				read_flag = False
			elif (t1 <= start_time and start_time < t2):
				read_flag = True
			elif (end_time < t1):
				read_flag = False

		elif read_flag:
			content_buffer += line.decode('utf-8')

	return re.sub(r'[\t\n]', '', content_buffer)

if __name__ == '__main__':
	print extract_content('YouTube Captions and Subtitles.en.vtt', '0:01:00', 10, 'second')