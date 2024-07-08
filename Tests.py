import unittest
from Transformations import calculate_overall_commute_quality

class TestTransformations(unittest.TestCase):

    def test_overall_commute_quality(self):
        overall_commute_quality = calculate_overall_commute_quality(3.25, 6.75, 14.75)
        self.assertEqual(overall_commute_quality.overall_commute_quality_score, 8.25)
        self.assertEqual(overall_commute_quality.overall_commute_quality, "Average")

if __name__ == '__main__':
    unittest.main()