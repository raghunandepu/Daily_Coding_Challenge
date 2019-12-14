"""Given 2 rectangles parallel to coordinate axes, find the area covered by them.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains 4 integers - xbl, ybl, xtr, ytr - the bottom-left and top-right coordinates of rectangle-1. The second line of each test case contains 4 integers - xbl, ybl, xtr, ytr - the bottom-left and top-right coordinates of rectangle-2. 

Constraints

1 <= T <= 10000 
-106 < x,y <= 106 
(xbl, ybl) < (xtr, ytr) 

Output Format

For each test case, print the area covered by the 2 rectangles, separated by newline. 

Sample Input 0

4
2 5 4 6
1 2 5 4
-4 -3 -2 5
-3 -5 1 3
1 0 3 5
2 3 5 8
-2 2 4 4
-3 1 5 5
Sample Output 0

10
42
23
32"""

t = int(input())
for tc in range(t):
  xbl1, ybl1, xtr1, ytr1 = map(int, input().split())
  xbl2, ybl2, xtr2, ytr2 = map(int, input().split())
  
  # xdist = abs(xtr1 - xbl1)
  # ydist = abs(ytr1 - ylb1)
  
  # Total area = sum of areas of rectangle1, rectange2 and with intersected area subracted as it appears twice in both rectangles.
  
  # Area of rectangle 1
  area1 = abs(xtr1 - xbl1) * abs(ytr1 - ybl1)
  
  # Area of rectangle 2
  area2 = abs(xtr2 - xbl2) * abs(ytr2 - ybl2)
  
  # Intersecting area
  #x_dist = min(xtr2, xtr1) - max(xbl2, xbl1) 
  #y_dist = min(ytr2, ytr1) - max(ybl2, ybl1)
  intersect_area = (min(xtr2, xtr1) - max(xbl2, xbl1)) * (min(ytr2, ytr1) - max(ybl2, ybl1))
  
  total_area = area1 + area2 - intersect_area
  print (total_area)
