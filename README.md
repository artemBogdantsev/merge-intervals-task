# Introduction
A code challenge task

## Input
A list of closed intervals, e.g. [2,19] [25,30] [14,23] [4,8]

**Note:** in a context of the picked language I assume that an interval is represented by an array of two elements - the lower and the upper border.

## Output
A list of merged intervals, e.g. [2,23] [25, 30]


## Realisation

To solve this task I will refer to the scanning line algorithm:
1. Pick all the borders (lower, upper) of each interval and put them into array/list
2. Assign 1 to those borders which are beginning of each interval
3. Assign -1 to those borders which are end of each interval
4. Sort an array/list ascending
5. Start "scanning" from the first element from left to right!
6. Use counter to have an information of how many intervals exist at the certain border.
7. If counter resets to 0 at the certain point then it is an end of interval. If counter changes to 1 then new interval begins

## Usage
### 1. Through unit test
- Please add your test cases to see that the MERGE function fulfils your requirements
- ``` > python unit_test.py```

### 2. Through CLI
- Please call the `merge.py` script from the console
- ``` > python merge.py -i "[interval 1] [interval 2] ... [interval N]"```
- **Note**: please use whitespaces as separator for the intervals in square brackets

## Results
1. Initial task performance
```
botem@Artems-MBP > ~/IdeaProjects/merge-intervals-task > master > python -m memory_profiler merge.py -i "[2, 19] [25, 30] [14, 23] [4, 8]"                                        
Intervals: [[2, 19], [25, 30], [14, 23], [4, 8]] <type 'list'>
Merge result: [[2, 23], [25, 30]] <type 'list'>
--- 0.0033469200 seconds ---
Filename: intervals.py

Line #    Mem usage    Increment   Line Contents
================================================
    14    9.363 MiB    9.363 MiB       @profile
    15                                 def merge(self):
```
2. Performance by adding more intervals
```
botem@Artems-MBP > ~/IdeaProjects/merge-intervals-task > master > python -m memory_profiler merge.py -i "[2, 19] [25, 30] [14, 23] [4, 8] [23, 25] [2,8] [-3, 5] [1,3] [34, 3435]"
Intervals: [[2, 19], [25, 30], [14, 23], [4, 8], [23, 25], [2, 8], [-3, 5], [1, 3], [34, 3435]] <type 'list'>
Merge result: [[-3, 30], [34, 3435]] <type 'list'>
--- 0.0046708584 seconds ---
Filename: intervals.py

Line #    Mem usage    Increment   Line Contents
================================================
    14    9.672 MiB    9.672 MiB       @profile
    15                                 def merge(self):
```
