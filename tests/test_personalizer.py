import unittest
import sys

# Add src to the path to allow imports from our src folder
sys.path.insert(0, './src')

from personalizer import personalize_problem
from problem_template import CORE_PROBLEM_TEMPLATE

class TestPersonalizer(unittest.TestCase):

    def test_personalize_for_sports(self):
        """
        Tests that the problem is correctly personalized for the 'sports' interest.
        """
        expected = "2 of the 6 soccer balls are blue. What fraction of the soccer balls are blue?"
        actual = personalize_problem(
            interest="sports",
            count=2,
            total_count=6,
            template=CORE_PROBLEM_TEMPLATE
        )
        self.assertEqual(actual, expected)

    def test_personalize_for_food(self):
        """
        Tests that the problem is correctly personalized for the 'food' interest.
        """
        expected = "4 of the 8 pizzas are pepperoni. What fraction of the pizzas are pepperoni?"
        actual = personalize_problem(
            interest="food",
            count=4,
            total_count=8,
            template=CORE_PROBLEM_TEMPLATE
        )
        self.assertEqual(actual, expected)

    def test_fallback_for_unknown_interest(self):
        """
        Tests that the function falls back to default values for an unknown interest.
        """
        expected = "1 of the 4 items are special. What fraction of the items are special?"
        actual = personalize_problem(
            interest="history",
            count=1,
            total_count=4,
            template=CORE_PROBLEM_TEMPLATE
        )
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
