# Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/

# Time = O(n) | Space = O(n)

def fizzBuzz(n: int):
  ans = []
  for i in range(1,n+1):
      if i % 5 == 0 and i % 3 == 0:
          ans.append("FizzBuzz")
      elif i % 5 ==0:
          ans.append("Buzz")
      elif i % 3 ==0:
          ans.append("Fizz")
      else:
          ans.append(str(i))
  return ans
          
print (fizzBuzz(5))