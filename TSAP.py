import tweepy
import wx
import speech_recognition as sr
import pyttsx3
from textblob import TextBlob
from statistics import *

def speakText(command):
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=(750,300), size=wx.Size(425, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Twitter Sentiment Analysis")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Enter the keyword that you want to search")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,20))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        if input == '':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio \n")
                speakText("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e)+"\n")
                speakText("Could not request results from Google Speech Recognition service")
        else:
            consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            subject = input
            speakText(subject)
            list = []
            neutral=0
            positive=0
            negative=0
            count =0
            for tweet in tweepy.Cursor(api.search, q=subject).items(1000):
                print(tweet.text)
                analysis = TextBlob(tweet.text)
                print(analysis.sentiment)
                list.append(analysis.sentiment.polarity)
                count+=1
            print ("Average Polarity: " + str(mean(list)) )   
            for i in list:
                if i==0.0:
                   neutral+=1
                if i>0.0:
                   positive+=1
                if i<0.0:
                   negative+=1
            print ("Total Neutral: " + str(neutral))
            speakText("Total Neutral: " + str(neutral))
            print ("Total Positive: " + str(positive))
            speakText("Total Positive: " + str(positive))
            print("Total Negative: " + str(negative))
            speakText("Total Negative: " + str(negative))
            print("Total Tweets Searched: " + str(count))
            speakText("Total Tweets Searched: " + str(count))

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()