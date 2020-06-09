 # Imports needed to connect to the Twitter API, perform sentiment analysis, and plot a chart
import sys 
from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt

# Keys needed to connect to the Twitter API which can be obatined by creating a Twitter developer account 
consumerKey = ''
consumerSecret = ''
accessToken = ''
accessTokenSecret = ''

# Authentication that allows for access between this program and Twitter
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

print()
keyword = input("Enter keyword that you would like analyzed: ")
print()

# Collects 300 tweets as a list based on keyword that the user entered
tweets = tweepy.Cursor(api.search, q=keyword, lang = "en").items(300)

# Keep count of positive, negative, and neutral tweets
positive = 0
negative = 0
neutral = 0 

for t in tweets:
  views = TextBlob(t.text)           # Perform analysis on the text of the tweet
  if views.sentiment.polarity == 0:
    neutral = neutral + 1
  elif views.sentiment.polarity > 0:
    positive = positive + 1
  elif views.sentiment.polarity < 0:
    negative = negative + 1

# Polarity measures how positive or negative something is (Range: -1 to 1)
# Negative number means negative sentiment and positive number means positive sentiment

# Calculates the percentages and rounds up to 2 decimal places

positivePer = round (100 * (float(positive)/float(300)), 2)
negativePer = round (100 * (float(negative)/float(300)), 2)
neutralPer = round (100 * (float(neutral)/float(300)), 2)

print ("Percentage of tweets with positive views:", positivePer)
print ("Percentage of tweets with negative views:", negativePer)
print ("Percentage of tweets with neutral views:", neutralPer)

# The following code is for producing the pie chart

plt.title('Twitter sentiment on keyword: ' + keyword + ' (Based on the analysis of 300 tweets)')
labels = ['Positive: '+ str(positivePer) +'%', 'Negative: '+ str(negativePer) +'%', 'Neutral: '+ str(neutralPer) +'%']
sizes = [positivePer, negativePer, neutralPer]
colors = ['red', 'green', 'blue']
plt.pie(sizes, colors=colors)
plt.legend(labels)
plt.show()

  
