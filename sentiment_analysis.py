from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
	
def get_afinn_score(line):
    """
    AFINN is a list of English words rated for valence with an integer
    between minus five (negative) and plus five (positive).
    """

    afinn = Afinn()
    score = afinn.score(line)    

    sentiment = ''
    if score >= 1.5:
        sentiment = 'Positive'
    else:
        if (score > - 1.5) and (score < 1.5):
            sentiment = 'Neutral'
        else:
            sentiment = 'Negative'		
		
    return sentiment
	
def get_NLTK_score(line):
    """
	Use NLTK Vader (Valence Aware Dictionary and sEntiment Reasoner)
	"""
	
    analyser = SentimentIntensityAnalyzer()
    snt = analyser.polarity_scores(line)
    score = float(snt['compound'])
    sentiment = ''
    if score >= 0.5:
        sentiment = 'Positive'
    else:
        if (score > - 0.5) and (score < 0.5):
            sentiment = 'Neutral'
        else:
            sentiment = 'Negative'		
		
    return sentiment

def get_sentiment(line):
    afinn_score = get_afinn_score(line)    
    NLTK_score = get_NLTK_score(line)	

	#If the scores are in agreement, return the afinn score. Otherwise return 'neutral' if they disagree
    if afinn_score == NLTK_score:
        return afinn_score
    else:
        return 'Neutral'
