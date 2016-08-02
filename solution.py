#!/usr/bin/python

DEBUG = False

num_strings = int(raw_input().strip())
for string_num in range(num_strings):
    string = raw_input().strip()
    if DEBUG: print "=" * 30
    if DEBUG: print "string %d : %s" % (string_num, string)
    charlist = list(string)
    newstring = ""
    tempstring = ""
    cost = 0
    for charnum, char in enumerate(charlist):
        if DEBUG: print "--- step %d ---" % charnum
        if DEBUG: print "char: %s" % char
        if DEBUG: print "newstring: %s" % newstring
        if DEBUG: print "tempstring: %s" % tempstring
        teststring = "%s%s" % (tempstring, char)
        if DEBUG: print "-"
        if DEBUG: print "testing %s" % teststring
        if teststring in newstring:
            tempstring = teststring
            if DEBUG: print "tempstring becomes: %s" % tempstring
            continue
        else:
            newstring += tempstring
            if char not in newstring:
                if DEBUG: print "cost just increased to %d"  % cost
                cost += 1
            newstring += char
            tempstring = ""
            if DEBUG: print "tempstring resets"
            if DEBUG: print "newstring becomes: %s" % newstring
            
    if DEBUG: print "final cost answer: ",
    print "%d" % cost
            

