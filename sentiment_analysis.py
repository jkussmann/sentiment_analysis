"""
This module uses multiple sentiment analysis functions and returns a
consolidated result
"""

from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_afinn_score(line):
    """
    AFINN is a list of English words rated for valence with an integer
    between minus five (negative) and plus five (positive).
    """

    afinn = Afinn()
    score = afinn.score(line)

    sentiment = ""
    if score >= 1.5:
        sentiment = "Positive"
    else:
        if -1.5 < score < 1.5:
            sentiment = "Neutral"
        else:
            sentiment = "Negative"

    return sentiment


def get_nltk_score(line):
    """
	Use NLTK Vader (Valence Aware Dictionary and sEntiment Reasoner)
	"""

    analyser = SentimentIntensityAnalyzer()
    snt = analyser.polarity_scores(line)
    score = float(snt["compound"])
    sentiment = ""
    if score >= 0.5:
        sentiment = "Positive"
    else:
        if -0.5 < score < 0.5:
            sentiment = "Neutral"
        else:
            sentiment = "Negative"

    return sentiment


def get_sentiment(line):
    """
	This function calls the nltk and spacy sentiment analysis functions
	"""
    afinn_score = get_afinn_score(line)
    nltk_score = get_nltk_score(line)
    final_score = ""

    # If the scores are in agreement, return the afinn score. Otherwise
    # return 'neutral' if they disagree
    if afinn_score == nltk_score:
        final_score = afinn_score
    else:
        final_score = "Neutral"

    return final_score
