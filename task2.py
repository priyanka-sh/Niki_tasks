def convert(A):
	ret = ''
        while A != 0:
            A = A-1
            temp = A%26
            A /= 26
            ret += chr(temp+ord('A'))
        return ret[::-1]
flag = 0
A = int(raw_input("Enter number1: "))
B = int(raw_input("Enter number2: "))
if(A>B or A<1 or  B<1 or  A>676 or B>676):
	print "Enter valid set of numbers"
	flag=1

if flag==0:
	for i in range(A,B+1):
		print "The "+str(i)+"th column is",convert(i)
