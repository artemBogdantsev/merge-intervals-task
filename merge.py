#!/usr/bin/python

import getopt, sys, intervals

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:", ["help", "intervals="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--intervals"):
            list_of_intervals = list(map(lambda x: map(int, x.strip(' ').split(',')), arg.strip('[').strip(']').split('] [')))
            print "Intervals:", list_of_intervals, type(list_of_intervals)
            result = intervals.Intervals(list_of_intervals).merge()
            print "Merge result:", result, type(result)
        else:
            assert False, "unhandled option"



def usage():
    print "Usage:\n" \
          "merge.py -i \"<intervals>\"\n" \
          "intervals are space separated: [a,c] [b, d]"

if __name__ == "__main__":
    main()