# TSAP

TSAP (Twitter-Sentiment Analysis using Python) is a script which search the most recent 1000 tweets that contain the desired keyword(celebrity, famous personality or any noun). The script then analyses each and every tweet and gives it a Float number between -1 to 1. At the end we get the total neutral, negative and positive tweets related to the keyword, as well as the mean.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install tweepy
pip install textblob
pip install wxPython
pip install SpeechRecognition
pip install pyttsx3
pip install PyAudio
```
1. After installing tweepy go to [Twitter Developer](https://developer.twitter.com/en) and apply for Twitter API to get started.
2. If there is problem in installing PyAudio, then go to the [link](https://www.lfd.uci.edu/~gohlke/pythonlibs/) and download the package file according to the system requirements and then try to install it.

## Usage

![](/TSAPInput.JPG)

![](/TSAPOutput.JPG)

1. First change the lines 48 to 51 by providing Consumer Key, Consumer Secret, Access Token and Access Token Secret.
2. There are two ways to give input - i) Write the keyword in given space and click Enter. ii) Click on Enter, provide keyword by voice command and then again click on Enter.