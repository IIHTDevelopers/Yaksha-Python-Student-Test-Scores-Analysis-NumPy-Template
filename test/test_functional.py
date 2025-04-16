import unittest
import numpy as np
from mainclass import TestScoresAnalysis
from test.TestUtils import TestUtils
from scipy import stats



class FunctionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.scores = [85, 90, 85, 75, 95, 80, 80]
        self.test_analysis = TestScoresAnalysis(self.scores)

    def test_mean_score(self):
        """Test if the mean score is calculated correctly"""
        obj = self.test_analysis.mean_score()
        expected_mean = np.mean(self.scores)
        test_obj = TestUtils()
        if obj == expected_mean:
            test_obj.yakshaAssert("TestMeanScore", True, "functional")
            print("TestMeanScore = Passed")
        else:
            test_obj.yakshaAssert("TestMeanScore", False, "functional")
            print("TestMeanScore = Failed")

    def test_median_score(self):
        """Test if the median score is calculated correctly"""
        obj = self.test_analysis.median_score()
        expected_median = np.median(self.scores)
        test_obj = TestUtils()
        if obj == expected_median:
            test_obj.yakshaAssert("TestMedianScore", True, "functional")
            print("TestMedianScore = Passed")
        else:
            test_obj.yakshaAssert("TestMedianScore", False, "functional")
            print("TestMedianScore = Failed")

    def test_mode_score(self):
        """Test if the mode score is calculated correctly"""
        obj = self.test_analysis.mode_score()
        # expected_mode = stats.mode(self.scores)[0][0]
        # expected_mode = stats.mode(self.scores, keepdims=False)[0][0]
        expected_mode = stats.mode(self.scores, keepdims=False)[0]
        test_obj = TestUtils()
        if obj == expected_mode:
            test_obj.yakshaAssert("TestModeScore", True, "functional")
            print("TestModeScore = Passed")
        else:
            test_obj.yakshaAssert("TestModeScore", False, "functional")
            print("TestModeScore = Failed")