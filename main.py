import sys
import sentiment_analysis as sa

def get_input():
	line = ''

	try:
		while (line != 'end'):
			line = input('\r\n' + 'Enter a sentence: ')
			if line == 'end':
				print ('Ending Program ...')
				sys.exit()
			else:
				print ('')
				print ('Afinn Sentiment: ')
				print (sa.get_afinn_score(line))
				print ('')
				print ('NLTK Vader Sentiment: ')
				print (sa.get_NLTK_score(line))
				print ('')
				print ('Consolidated Sentiment:')
				print (sa.get_sentiment(line))

	except KeyboardInterrupt:
		sys.exit()

def main():
	"""
	This is the main entry point for the program
	"""    

	get_input()

if __name__ == "__main__":
	main()