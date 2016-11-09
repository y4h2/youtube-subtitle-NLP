#!/usr/bin/env python
from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        # if msg == 'video doesn\'t have subtitles':
        #     print 'Error: no subtitles'
        # else:
        #     print(msg)
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading.')
    if d['status'] == 'error':
        print('Error')

# no subtitle will only lead a warning
# wrong links will lead an error
def subtitle_downloader(link):
    # website = link.split('v=')[0]
    # id = link.split('v=')[1]
    # if (id.length() != 11):
    #     return 'wrong length of video id'

    subtitle_path = 'resources/subtitles/'
    subtitle_tmpl = '%(title)s.%(ext)s'
    ydl_opts = {
        'logger': MyLogger(),
        'progress_hooks': [my_hook], #only works when downloading videos
        'subtitlesformat': 'vtt',
        'subtitleslangs': ['en'],
        'skip_download': True,
        # 'allsubtitles': True,
        'writesubtitles': True,
        'outtmpl': subtitle_path + subtitle_tmpl, #DEFAULT_OUTTMPL = '%(title)s-%(id)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link]) #the id should be exactly 11 characters

if __name__ == '__main__':
    link = 'https://www.youtube.com/watch?v=n5sB19UTcdA'
    subtitle_downloader(link)
    # https://www.youtube.com/watch?v=Ye8mB6VsUHw
    # no subtitle
    # https://www.youtube.com/watch?v=n5BB19UTcdA