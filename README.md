# Sentiment Analysis
This code performs sentiment analysis using NLTK Vader and Afinn. The results of each one is consolidated. If there is disagreement, 'neutral' is used.

## Getting Started

This code is initially written to run on a Windows 10 environment. The program is run from the command line and any IDE can be used.

### Prerequisites

What things you need to install the software and how to install them
* Python 3 (https://www.python.org/downloads/windows/)
* NLTK (https://www.nltk.org/)
* Afinn (https://github.com/fnielsen/afinn)

## Running the code

Open a command line window and change to the directory the code is located. 

Positive
```
c:\sentiment_analysis>python main.py

Enter a sentence: That was the best book I have read in a long time.

Afinn Sentiment:
Positive

NLTK Vader Sentiment:
Positive

Consolidated Sentiment:
Positive

Enter a sentence:
```

Mixed results
```
Enter a sentence: I have seen better movies than this.

Afinn Sentiment:
Positive

NLTK Vader Sentiment:
Neutral

Consolidated Sentiment:
Neutral

Enter a sentence:
```

Negative
```
Enter a sentence: Don't go to that restaurant, it's the worst ever.

Afinn Sentiment:
Negative

NLTK Vader Sentiment:
Negative

Consolidated Sentiment:
Negative

Enter a sentence: end
Ending Program ...
```

## Testing

To run unit tests on the code, open a command line window and change to the directory where the code is located.

```
C:\sentiment_analysis>python test_sa_unittest.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.142s

OK
```

## Author

* **John Kussmann** - *Initial work*