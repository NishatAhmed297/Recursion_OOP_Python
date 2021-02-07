def sum(arr):
  ## This function has a time complexity of O(n^2) because of iterating everytime we split the array into "rest" of the chunk --Line 19 of this file
  print(_sum(arr))
  ## We give an identifier to recursion function to keep track of the index and not iterating at every step. So time complexity is now O(n).
  print(__sum(arr,0))
   
# Method 1
def _sum(n):
  ## Setting up our base case, that when array of integers become empty then return 0.
  if len(n) == 0:
    return 0
  
  ## Break down the array and call the function with rest of the chunk.
  return n[0] + _sum(n[1:])
 
 # Method 2
 def __sum(arr,idx):
  if(idx == len(arr)):
    return 0
  return arr[idx] + __sum(arr,idx+1)  
 
 ##Test Case
 sum([1,-2,3,-4])
