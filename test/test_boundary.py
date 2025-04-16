import unittest
import numpy as np
from mainclass import TestScoresAnalysis
from test.TestUtils import TestUtils


class BoundaryTests(unittest.TestCase):
    def test_single_element(self):
        """Test with only one test score"""
        single_data = TestScoresAnalysis([85])
        obj_mean = single_data.mean_score()
        obj_median = single_data.median_score()
        obj_mode = single_data.mode_score()
        test_obj = TestUtils()
        if obj_mean == obj_median == obj_mode == 85:
            test_obj.yakshaAssert("TestSingleElement", True, "boundary")
            print("TestSingleElement = Passed")
        else:
            test_obj.yakshaAssert("TestSingleElement", False, "boundary")
            print("TestSingleElement = Failed")

    def test_large_data_set(self):
        """Test with a very large data set"""
        large_data = TestScoresAnalysis([i for i in range(1, 100001)])
        try:
            obj_mean = large_data.mean_score()
            obj_median = large_data.median_score()
            obj_mode = large_data.mode_score()
            if not obj_mean:
                test_obj.yakshaAssert("TestLargeDataSet", False, "boundary")
                print("TestLargeDataSet = Failed")
                return
            test_obj = TestUtils()
            test_obj.yakshaAssert("TestLargeDataSet", True, "boundary")
            print("TestLargeDataSet = Passed")
        except:
            test_obj = TestUtils()
            test_obj.yakshaAssert("TestLargeDataSet", False, "boundary")
            print("TestLargeDataSet = Failed")
