def fizzBuzz(A):
        result = [0 for i in range(A)]
        for i in range(1,A+1):
            if i % 3 ==0 and i % 5 == 0:
                result[i-1] = "FizzBuzz"
                continue
            
            elif (i % 3 == 0):
                result[i-1] = "Fizz"
                continue
            
            elif (i % 5 == 0):
                result[i-1] = "Buzz"
                continue
            result[i-1] = str(i)
        return result

print (fizzBuzz(15))