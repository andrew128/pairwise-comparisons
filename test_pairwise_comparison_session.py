import unittest
from pairwise_comparison_session import PairwiseComparisonSession

class TestPairwiseComparisonSession(unittest.TestCase):
    def setUp(self):
        """Set up a fresh PairwiseComparisonSession before each test"""
        self.session = PairwiseComparisonSession()

    def test_store_options(self):
        """Test storing and retrieving options"""
        options = ["Apple", "Banana", "Orange"]
        self.session.store_options(options)
        
        # Test that options are stored correctly
        self.assertEqual(self.session.get_option(0), "Apple")
        self.assertEqual(self.session.get_option(1), "Banana")
        self.assertEqual(self.session.get_option(2), "Orange")

    def test_store_result_from_user(self):
        """Test storing user votes"""
        options = ["Apple", "Banana", "Orange"]
        self.session.store_options(options)
        
        # Test initial vote
        self.session.store_result_from_user(0)
        self.assertEqual(self.session.option_score[0], 1)
        
        # Test multiple votes for same option
        self.session.store_result_from_user(0)
        self.assertEqual(self.session.option_score[0], 2)

    def test_generate_results(self):
        """Test results generation and sorting"""
        options = ["Apple", "Banana", "Orange"]
        self.session.store_options(options)
        
        # Create some test votes
        self.session.store_result_from_user(0)  # Apple: 1
        self.session.store_result_from_user(0)  # Apple: 2
        self.session.store_result_from_user(1)  # Banana: 1
        
        results = self.session.generate_results()
        
        # Check results are sorted by score
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0], (0, "Apple", 2))    # Highest score
        self.assertEqual(results[1], (1, "Banana", 1))   # Second
        self.assertEqual(results[2], (2, "Orange", 0))   # No votes

    def test_empty_options(self):
        """Test behavior with empty options list"""
        self.session.store_options([])
        results = self.session.generate_results()
        self.assertEqual(results, [])

if __name__ == '__main__':
    unittest.main()