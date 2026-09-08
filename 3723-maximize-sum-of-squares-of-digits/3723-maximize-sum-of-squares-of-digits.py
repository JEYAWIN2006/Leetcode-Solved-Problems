class Solution:
  def maxSumOfSquares(self, num: int, sum: int) -> str:
    res = []
    while num and sum:
      if sum >= 9:
        res.append('9')
        num -= 1
        sum -= 9
      else:
        res.append(str(sum))
        num -= 1
        sum = 0
    
    if num == 0 and sum == 0:
      return ''.join(res)
    
    if num == 0:
      return ''
    
    if sum == 0:
      res.append('0' * num)
      return ''.join(res)