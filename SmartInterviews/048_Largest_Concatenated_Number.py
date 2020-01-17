# Approach:
# we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y). If XY is larger, then X should come before Y in output, else Y should come before. For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.

# Time complexity : 
"""
O(nlgn)

Although we are doing extra work in our comparator, it is only by a constant factor. Therefore, the overall runtime is dominated by the complexity of sort, which is O(nlgn) in Python and Java.

Space complexity : O(n)

Here, we allocate O(n) additional space to store the copy of nums """

# Implementing a custom class to be used in comparision later.
class LargerNumKey(str):
    def __lt__(x, y):
      """ Changing default 'less than' function to be used in sort"""
        return x+y > y+x

def largestNumber(arr):
        largest_num = ''.join(sorted(map(str, arr), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
        
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = largestNumber(arr)
    print (result)