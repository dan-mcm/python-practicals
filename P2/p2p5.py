animals = 'herd of elephants'

x=2
y=2

seg = animals [x:y]

#prints result when x and y are the same (blank returned)
print ('Segment is:',seg)

x=7
y=3

seg = animals[x:y]

#prints result when x is greater than y (blank returned)
print ('Segment is:',seg)

x=5
y=6

seg = animals[:y]

#what happens when x is omitted ('herd o' returned - string represented by y)
print ('Segment is:',seg)

x=5
y=5

seg = animals[x:]

#what happens when y is omitted ('of elephants' returned - string represented by x)
print ('Segment is:',seg)

x=5
y=5

seg = animals[:]

#what happens when x and y are omitted ('herd of elephants returned' - full string returned)
print ('Segment is:',seg)
