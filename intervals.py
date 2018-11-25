class Intervals:
    def __init__(self, intervals):
        self.intervals = intervals
        self.cnt = 0
        self.type_start = 1
        self.type_end = -1
        self.borders = []
        self.result = []
        self.start_border = ''

    def print_intervals(self):
        print(self.intervals)

    def merge(self):
        '''
        Implementation of the merge function based on the scanning line algorithm

        :return:
        '''

        # first we loop through all intervals and pick their start and end borders adding type of this border
        for interval in self.intervals:
            self.borders.append([interval[0], self.type_start])
            self.borders.append([interval[1], self.type_end])

        # using python's sort function on the list to sort all borders ascending
        self.borders.sort()

        # second loop through the sorted borders and doing recalculation on interval overlaps
        for border in self.borders:
            # if this is a starting point or previous interval ended we start from the new one
            if self.cnt == 0:
                self.start_border = border[0]

            # calculate how many overlaps(cnt > 1) we have
            self.cnt = self.cnt + border[1]

            # no overlaps(cnt > 1) and we reached the end of interval (start(1) + end(-1) = 0)
            if self.cnt == 0:
                end_border = border[0]

                # as we reached the end border of non-overlapped interval, it is time to store it in a final list
                self.result.append([self.start_border, end_border])

        return self.result
