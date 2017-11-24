""" Goal: Use sentiment analysis to aid analysis """
from textblob import TextBlob

def get_sentiment(sentence):
    """Get the polarity and subjectivity of a sentence.
    
    [description]
    
    Arguments:
        A string of any size.
    
    Returns:
        A tuple. The first element is polarity with range in [-1.0, 1.0]
        The second element is subjectivity, ranging from 0 to 1.0.
    
    Example:
        >>> s = TextBlob("I love you") 
        >>> s.sentiment
        >>> Sentiment(polarity=0.5, subjectivity=0.6)
        
        >>> s = TextBlob("I hate you")
        >>> s.sentiment
        >>> Sentiment(polarity=-0.8, subjectivity=0.9)

    """
    return TextBlob(sentence).sentiment 