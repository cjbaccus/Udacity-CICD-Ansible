def printAllKLength(set, k):
	n = len(set)
	printAllKLengthRec(set, "", n, k)
def printAllKLengthRec(set, prefix, n, k):
	if (k == 0) :
		print(prefix)
		return
	for i in range(n):
		newPrefix = prefix + set[i]
		printAllKLengthRec(set, newPrefix, n, k - 1)

# Driver Code
if __name__ == "__main__":
	
	print("First Test")
	set1 = ['1qaz','2wsx','3edc','4rfv','!QAZ','@WSX','#EDC','$RFV']
	k = 4
	printAllKLength(set1, k)
	
