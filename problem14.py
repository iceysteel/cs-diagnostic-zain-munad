#this one was pretty fun actually
def most_common(inputstring, k):
	table = {}
	for word in inputstring.split():
		if table.get(word):
			table[word] = table[word] + 1
		else:
			table[word] = 0
			table[word] = table[word] + 1
	#at this point the table turns into an array due to how sorted works
	table = sorted(table, key=table.get)
	table.reverse()
	#print table
	for x in range(0, k):
		print table[x]


instring = '''
Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Python and other third party extensions. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate version that returns an iterator.

'''

most_common(instring, 7)