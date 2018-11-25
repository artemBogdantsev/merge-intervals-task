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