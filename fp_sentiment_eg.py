from textblob import TextBlob as tb

eg1 = tb('I love you this is wonderful!')
eg1.sentiment

# Out[]: Sentiment(polarity=0.75, subjectivity=0.8)

eg2 = tb('That is certainly false and you are ugly')
eg2.sentiment

# Out[]: Sentiment(polarity=-0.55, subjectivity=0.8)

eg3 = tb('two plus two is four.')
eg3.sentiment

# Out[]: Sentiment(polarity=0.0, subjectivity=0.0)