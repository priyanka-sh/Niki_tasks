def sortbylength(list1):
	list1.sort(key=len)
	print 'Sorted list is: ',list1
n=int(raw_input('Enter number of elements in list: '))
mainlist=[]
for i in range(0,n):
	word=raw_input('enter elements: ')
	mainlist.append(word)

sortbylength(mainlist)

	
 
