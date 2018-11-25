import unittest
import intervals

class MergeTest(unittest.TestCase):

    def test_right_result(self):
        '''
        Unittest to Get the right result
        '''

        myIntervals = [[2, 19], [25, 30], [14, 23], [4, 8]]
        myCorrectResult = [[2, 23], [25, 30]]

        myIntervals2 = [[2, 19], [25, 30], [14, 23], [4, 8], [-3, 2]]
        myCorrectResult2 = [[-3, 23], [25, 30]]

        myIntervals3 = [[2, 19], [25, 30], [14, 23], [4, 8], [23, 25]]
        myCorrectResult3 = [[2, 30]]

        self.assertEqual(intervals.Intervals(myIntervals).merge(), myCorrectResult)
        self.assertEqual(intervals.Intervals(myIntervals2).merge(), myCorrectResult2)
        self.assertEqual(intervals.Intervals(myIntervals3).merge(), myCorrectResult3)

    def test_wrong_result(self):
        '''
        Unittest to fail with the wrong result
        '''

        myIntervals = [[2, 19], [25, 30], [14, 23], [4, 8], [23, 25]]
        myCorrectResult = [[2, 23], [25, 30]]

        self.assertNotEqual(intervals.Intervals(myIntervals).merge(), myCorrectResult)

if __name__ == '__main__':
    unittest.main()
