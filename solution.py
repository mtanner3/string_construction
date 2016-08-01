#!/usr/bin/python

num_strings = int(raw_input().strip())
for string_num in range(num_strings):
    string = raw_input().strip()
    print "string %d : %s" % (string_num, string)
