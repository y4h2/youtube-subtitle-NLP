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
- types: 
  - song liric
  - movie dialog
  - speech
  - describe words
- the feature of subtitle is more close to movie review rather than twitter data
- may contain people character or name in the subtitles

# The problem of sentiment analysis
1. normal text just calculate the sentiment based on the number of  



# Useful dataset
- https://inclass.kaggle.com/c/si650winter11/data 
  get the traning data:  
  7086 lines, labeled with 0|1, 0 for negative, 1 for positive

- http://help.sentiment140.com/for-students/
  the stanford link  
  The data is a CSV with emoticons removed. Data file format has 6 fields:
  0 - the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
  1 - the id of the tweet (2087)
  2 - the date of the tweet (Sat May 16 23:58:44 UTC 2009)
  3 - the query (lyx). If there is no query, then this value is NO_QUERY.
  4 - the user that tweeted (robotickilldozr)
  5 - the text of the tweet (Lyx is cool)

- http://ai.stanford.edu/~amaas/data/sentiment/
  movie review dataset
  much cleaner than tweet data  
  a set of 25,000 highly polar movie reviews for training, and 25,000 for testing. 

- nltk.corpus.movie_reviews  
  paragraph level labelled data  
  1000 positive movie reviews and 1000 negtive movie reviews  
  easy to use, but it has less data

- https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences
  sentence level dataset  
  Score: 1 (positive) or 0 (negative)
  Source: imdb.com, amazon.com, yelp.com. Each website, 500 positive and 500 negative sentences. The text sentences are extracted from reviews of products, movies, and restaurants.



## Twitter sentiment dataset
- keep the sentiment and content column
- remove @... tag
- remove http links
- remove # tags
- sentiment range from 0-4
- contain lots of unformal words


## movie review dataset
- much cleaner than twitter data
- data are stored in files
- dataset is larger
- sentiment range from 0-10


# Sentiment Algorithm
## Naive Bayes algorithm
calculate the probility of the occurance of the sentiment word. Every word appear in the positive and negative with probility, based on this probility, the model can predict the sentiment of a sentence with all words in it.

Can provide both sentence and paragraph level sentiment analysis

## VADER
rule-based algorithm

## CoreNLP
only provide sentence level classify

API: https://algorithmia.com/algorithms/nlp/SentimentAnalysis  
Pricing: 10k calls = $1.08 USD

OR

use py-corenlp
```sh

```


## Evaluation Result
### CoreNLP
**Sentence Level**

Amazon Evaluation  
0.75769186114
0.679


Amazon Evaluation  
0.721432519418
0.645


Amazon Evaluation  
0.752129223853
0.69

### VADER
**Sentence Level**

Amazon Evaluation  
0.75769186114
0.679


Yelp Evaluation  
0.721432519418
0.645


Imdb Evaluation  
0.752129223853
0.69

**Paragraph Level**

Movie Review Evaluation  
0.622662172869
0.6365


# Named Entity Recognizer (NER)
The technique is already mature

# Topic Detect
## RAKE

## TextRank
graph-based algorithm


# Benchmark
training set is used for trainning the supervise model, the test set can be used to evaluate the performance of different algorithms.

