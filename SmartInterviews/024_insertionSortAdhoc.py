# https://www.hackerrank.com/contests/smart-interviews/challenges/si-insertion-sort
"""Implement Insertion Sort and print the index at which the ith element gets inserted [i>=1].

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - size of the array. The next line contains N integers - elements of the array.

Constraints

1 <= T <= 100 
2 <= N <= 100 
-1000 <= ar[i] <= 1000 

Output Format

For each test case, print the index at which the ith element gets inserted [i>=1], separated by space. Separate the output of different tests by newline.

Sample Input 0

4
8
176 -272 -272 -45 269 -327 -945 176 
2
-274 161
7
274 204 -161 481 -606 -767 -351
2
154 -109
Sample Output 0

0 1 2 4 0 0 6 
1 
0 0 3 0 0 2 
0 
"""
def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        j = i
        while (j > 0 and array[j] < array[j-1]):
            print (j-1)
            swap(j, j-1, array)
            j -= 1
    #return array

def swap (i, j, array):
    array[i], array[j] = array[j], array[i]
    
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(insertionSort(arr))