import sys
def sortbylength(list1):
	list1.sort(key=len)
	print 'Sorted list is: ',list1
print "Enter the list of strings, enter after each string, Ctrl+D when done entering"
mainlist=sys.stdin.readlines()
mainlist = [i[:-1] for i in mainlist]
sortbylength(mainlist)

	
 
