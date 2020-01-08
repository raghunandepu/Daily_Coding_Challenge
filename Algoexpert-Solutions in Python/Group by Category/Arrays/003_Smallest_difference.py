# https://www.algoexpert.io/questions/Smallest%20Difference

"""
Smallest Difference
​
Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers (one from the first array, one from the second array) whose absolute difference is closest to zero. The function should return an array containing these two numbers, with the number from the first array in the first position. Assume that there will only be one pair of numbers with the smallest difference.
​
Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Sample output: [28, 26]"""

# O(nlog(n) + mlog(m)) time | O(1) space
# for first array sorting + for second array sorting time

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort() # sort in place
	arrayTwo.sort()
	
	idxOne = 0
	idxTwo = 0
	smallest = float("inf") # Infinity to compare with our differences later
	current = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo += 1
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair