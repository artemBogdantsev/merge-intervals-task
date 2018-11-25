import unittest
import intervals

class MergeTest(unittest.TestCase):

    def test_right_result(self):
        '''
        Unittest to Get the right result
        '''

        myIntervals = [[2, 19], [25, 30], [14, 23], [4, 8]]
        myCorrectResult = [[2, 23], [25, 30]]
        self.MergeObj = intervals.Intervals(myIntervals)

        self.assertEqual(self.MergeObj.merge(), myCorrectResult)

    def test_wrong_result(self):
        '''
        Unittest to Get the right result
        '''

        myIntervals = [[2, 19], [25, 30], [14, 23], [4, 8], [23, 25]]
        myCorrectResult = [[2, 23], [25, 30]]
        self.MergeObj = intervals.Intervals(myIntervals)

        self.assertNotEqual(self.MergeObj.merge(), myCorrectResult)

if __name__ == '__main__':
    unittest.main()