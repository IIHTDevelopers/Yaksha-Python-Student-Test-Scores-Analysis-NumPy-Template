import unittest
from mainclass import TestScoresAnalysis
from test.TestUtils import TestUtils
import numpy as np

class ExceptionalTests(unittest.TestCase):
    def test_empty_data(self):
        """Test handling of empty scores array"""
        test_obj = TestUtils()
        try:
            empty_data = TestScoresAnalysis([])
            test_obj.yakshaAssert("TestEmptyData", False, "exceptional")
            print("TestEmptyData = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyData", True, "exceptional")
            print("TestEmptyData = Passed")

    def test_invalid_data_type(self):
        """Test handling of invalid data type (string instead of integers)"""
        test_obj = TestUtils()
        try:
            invalid_data = TestScoresAnalysis(["85", "90", "75", "80", "sdcsd"])
            test_obj.yakshaAssert("TestInvalidDataType", False, "exceptional")
            print("TestInvalidDataType = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestInvalidDataType", True, "exceptional")
            print("TestInvalidDataType = Passed")
