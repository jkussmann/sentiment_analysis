"""
Unit tests for the sentiment analysis functions
"""

import unittest
from sentiment_analysis import (
    get_afinn_score,
    get_nltk_score,
    get_sentiment,
)


class TestSA(unittest.TestCase):
    """
    Class for testing sentiment analysis
    """

    def test_afinn_positive(self):
        """
        Tests for Afinn with a positive result
        """
        self.assertEqual(
            get_afinn_score(
                "That was the best book I have read in a long time."
            ),
            'Positive',
        )

    def test_afinn_negative(self):
        """
        Tests for Afinn with a negative result
        """
        self.assertEqual(
            get_afinn_score(
                "Don't go to that restaurant, it's the worst ever."
            ),
            'Negative',
        )

    def test_nltk_positive(self):
        """
        Test for NLTK with a positive result
        """
        self.assertEqual(
            get_nltk_score(
                "That was the best book I have read in a long time."
            ),
            'Positive',
        )

    def test_nltk_negative(self):
        """
        Test for NLTK with a negative result
        """
        self.assertEqual(
            get_nltk_score(
                "Don't go to that restaurant, it's the worst ever."
            ),
            'Negative',
        )

    def test_consolidated_positive(self):
        """
        Test for the consolidation function with a positive result
        """
        self.assertEqual(
            get_sentiment(
                "That was the best book I have read in a long time."
            ),
            'Positive',
        )

    def test_consolidated_negative(self):
        """
        Test for the consolidation function with a negative result
        """
        self.assertEqual(
            get_sentiment(
                "Don't go to that restaurant, it's the worst ever."
            ),
            'Negative',
        )

    def test_consolidated_neutral(self):
        """
        Test for the consolidation function with a neutral result
        """
        self.assertEqual(
            get_sentiment(
                "I have seen better movies than this."
            ),
            'Neutral',
        )


if __name__ == "__main__":
    unittest.main()
