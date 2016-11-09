#!/usr/bin/env python
from __future__ import unicode_literals

import unittest
import sys, re
from cStringIO import StringIO
sys.path.append("../")
from subtitle_downloader import subtitle_downloader
from subtitle_extractor import extract_content

class TestSubtitlesDownloader(unittest.TestCase):

	def test_nosubtitles(self):
		# redirect std.out to the stream
		old_stdout = sys.stdout
		sys.stdout = mystdout = StringIO()
		subtitle_downloader('https://www.youtube.com/watch?v=n5BB19UTcdA')
		sys.stdout = old_stdout
		self.assertEqual(mystdout.getvalue().strip(), 'video doesn\'t have subtitles')


	def test_subtitle_extractor(self):
		test_result = "in my own language.\
		As a video uploader, this means you can reach\
		to people all over the world,\
		irrespective of language.\
		[Hiroto, Bedhead]\
		You can upload multiple tracks like English and French,\
		and viewers can choose the track they like.\
		[Toliver, Japanese Learner]\
		For example, if you enjoy using YouTube in French,\
		"
		extract_result = extract_content('YouTube Captions and Subtitles.en.vtt', '0:01:00', 10, 'second')
		self.assertEqual(re.sub(r'\s', '', extract_result), re.sub(r'\s', '', test_result))


if __name__ == '__main__':
	unittest.main()