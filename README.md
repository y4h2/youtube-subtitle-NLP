# youtube-subtitle-NLP
NLP analysis of youtube subtitles


# Installed Packages
- youtube-dl


# youtube-dl options
refer to https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L129

used in the project:
    - writesubtitles:    Write the video subtitles to a file
    - writeautomaticsub: Write the automatically generated subtitles to a file
    - allsubtitles:      Downloads all the subtitles of the video
                       (requires writesubtitles or writeautomaticsub)
    - listsubtitles:     Lists all available subtitles for the video
    - subtitlesformat:   The format code for subtitles
    - subtitleslangs:    List of languages of the subtitles to download
    - skip_download:     Skip the actual download of the video file

# The features of subtitle data
- may contain 

# The problem of sentiment analysis
1. normal text just calculate the sentiment based on the number of  



# Useful dataset
- https://inclass.kaggle.com/c/si650winter11/data 
  get the traning data:  
  7086 lines, labeled with 0|1, 0 for negative, 1 for positive

- 