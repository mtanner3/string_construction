#!/usr/bin/python

num_strings = int(raw_input().strip())
for string_num in range(num_strings):
    string = raw_input().strip()
    charlist = list(string)
    newstring = charlist.pop(0)
    tempstring = None
    cost = 0
    for charnum, char in enumerate(charlist):
        if tempstring is not None:
            startpos = 0
            done = False
            while done is False:
                location = newstring.find(tempstring, startpos)
                end_plus_one = location + len(tempstring)
                if location > -1 and end_plus_one < len(newstring):
                    if newstring[end_plus_one] == char:
                        tempstring += char
                    else:
                        startpos = location
                else:
                    done = True
        else: 
            if char in newstring:
                tempstring = char
            else:
                if tempstring is not None:
                    newstring += tempstring
                newstring += char
                tempstring = None
                cost += 1
    print "%d" % cost

