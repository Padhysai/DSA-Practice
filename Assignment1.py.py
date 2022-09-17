'''
Question -1

Compute and return the square root of x, where x is guaranteed to be a non-negative
integer. And since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned. Also, talk about the time complexity of your
code.

Question - 2

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad. Suppose you have n version and you want to find out the first bad one,
which causes all the following ones to be bad. Also, talk about the time complexity of
your code.

Question - 3

Given a positive integer num, write a program that returns True if num is a perfect
square else return False. Do not use built-in functions like sqrt. Also, talk about the time
complexity of your code.
'''
class Search:

  def findIntSquare(self, num):
    low = 1 
    high = num//2
    ans = 1
    
    while(low <= high):
      mid = low + (high - low)//2
      
      if(mid*mid == num):
        ans = mid
        return ans
      
      if(mid*mid > num):
        high = mid - 1 
        
      else:
        ans = mid
        low = mid + 1
    return ans

  def findFirstBadVersion(self,arr):
    low = 0
    high = len(arr) - 1
    ans = -1
    
    while(low <= high):
      mid = low + (high - low)//2
      
      if(arr[mid] == 1):
        ans = mid
        high = mid - 1
      else:
        low = mid + 1
    return ans

  def findPerfectSquare(self,num):
    low = 0
    high = num//2
    
    while(low <= high):
      mid = low + (high - low)//2
      
      if(mid*mid == num):
        return True
      
      if(mid*mid < num):
        low = mid + 1
      else:
        high = mid - 1
    return False

'''
Time complexity:
As we are applying Binary search for all the above problems, We will loop through the given array log n times.

Question 1 : Tc = O(log n/2), Where n is given int
Question 2 : Tc = O(log n), Where n is length of input array 
Question 3 : Tc = O(log n/2), Where n is given int
'''

