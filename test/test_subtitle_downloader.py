#!/usr/bin/env python
from __future__ import unicode_literals

import unittest
import sys
from cStringIO import StringIO
sys.path.append("../")
from subtitle_downloader import subtitle_downloader

class TestSubtitlesDownloader(unittest.TestCase):

	def test_nosubtitles(self):
		# redirect std.out to the stream
		old_stdout = sys.stdout
		sys.stdout = mystdout = StringIO()
		subtitle_downloader('https://www.youtube.com/watch?v=n5BB19UTcdA')
		sys.stdout = old_stdout
		self.assertEqual(mystdout.getvalue().strip(), 'video doesn\'t have subtitles')


if __name__ == '__main__':
	unittest.main()