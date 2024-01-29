
# from functools import reduce
# from typing import List

# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         l=1;
#         r=len(ratings)-2;
#         candies = [1] * len(ratings);
#         rightCandy = 1;

        # while l < len(ratings):
        #     if(ratings[l] > ratings[l-1]):
        #         candies[l] = candies[l-1]+1;
        #     l+=1
        # print(r)
        # while r >= 0:
        #     if(ratings[r] > ratings[r+1]):
        #         rightCandy+=1
        #         candies[r]=max(candies[r],rightCandy)
        #     else: 
        #         rightCandy =1
        #     r-=1


        # for x in range(1, len(ratings)):
        #     if(ratings[x] > ratings[x-1]):
        #         candies[x] = candies[x-1]+1;
        # for x in range (len(ratings)-2, -1,-1):
        #     if(ratings[x] > ratings[x+1]):
        #         rightCandy +=1
        #         candies[x] = max(candies[x], rightCandy);
        #     else:
        #         rightCandy =1
        # sum = reduce(lambda a,b: a + b, candies)

        # return sum;
# b = Solution()
# print(b.candy([1,3,2,2,1]))
# from typing import List


# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         result = [];
#         line = [];
#         width = 0;
#         for w in words:
#             if width + len(w) + len(line) > maxWidth:
#                 for i in range(maxWidth - width): line[i % (len(line) - 1 or 1)] += ' '
#                 result, line, width = result + [''.join(line)], [], 0
#             line += [w]
#             width += len(w)
#         return result + [' '.join(line).ljust(maxWidth)];


# b = Solution();
# print(b.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         res = True
#         temp = ''
#         for word in s:
#            if(word.isalpha() or word.isnumeric()):
#                temp += word
#         temp = temp.lower()
#         print(temp)
#         left = 0
#         right = len(temp)-1
#         while left <= right:
#             if(temp[left] != temp[right]):
#                 res = False
#                 return res
#             left +=1
#             right -=1
#         return res

# b = Solution();
# print(b.isPalindrome("0P"))

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         currentIndex = 0
#         for c in t:
#            if currentIndex == len(s): break
#            if(c == s[currentIndex]) : currentIndex+=1            

#         return currentIndex == len(s)
    
# b = Solution();
# print(b.isSubsequence("axc","ahbgdc"))

# from typing import List

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left, right = 0, len(numbers)-1

#         while left < right:
#             if(numbers[left] + numbers[right] == target):
#                 return [left+1,right+1]
#             elif(numbers[left] + numbers[right] > target):
#                 right-=1
#             elif(numbers[left] + numbers[right] < target):
#                 left+=1

# b = Solution()
# print(b.twoSum([2,3,4],6))

# from typing import List

# class Solution:
#     def helpTudor(self, times: int) -> List[int]:
        

#         res = []
#         for time in range(times):
#             a= input()
#             b= input()
#             res.append(a+b)
#         return res
    

# b = Solution()
# b.helpTudor(2)

# from typing import List
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left, right = 0 , len(height)-1
#         maxAmountWater = 0

#         while left<= right:
#             if(height[left] >= height[right]):
#                 maxAmountWater = max(maxAmountWater, height[right] * (right - left))
#                 right-=1
#             else:
#                 maxAmountWater = max(maxAmountWater, height[left] * (right - left))
#                 left +=1
#         return maxAmountWater
# b = Solution()
# print(b.maxArea([1,8,6,2,5,4,8,3,7]))


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left, right = 0 , len(height)-1
#         maxAmountWater = 0

#         while left<= right:
#             temp=0
#             if(height[left]<=height[right]) : 
#                 print(height[left])
#                 temp = height[left] * (left - right)
#             else: 
#                 print(height[right])
#                 temp = height[right] * (left-right )

#             if(maxAmountWater< temp): maxAmountWater = temp
#             left +=1
        
#         return maxAmountWater

# from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]: 
#         nums.sort()
#         answer = []

#         for i in range(len(nums)-2):
#             if nums[i]>0:
#                 break
#             if i>0 and nums[i] == nums[i-1]:
#                 continue
#             left=i+1
#             right=len(nums)-1
#             while(left<right):
#                 total = nums[i] + nums[left] + nums[right]
#                 if(total > 0):
#                     right-=1
#                 elif(total < 0):
#                     left+=1
#                 else:
#                     triplet = [nums[i],nums[left], nums[right]]
#                     answer.append(triplet)
#                     while left<right and nums[left] == triplet[1]:
#                         left +=1
#                     while left<right and nums[right] == triplet[2]:
#                         right -=1
#         return answer
            

# b = Solution()
# print(b.threeSum([-1,0,1,2,-1,-4]))

# from typing import List

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         passivePointer, activePointer, temp, res = 0 , 0 , 0, len(nums) + 1

#         while activePointer < len(nums):
#             temp += nums[activePointer]
#             activePointer += 1

#             while temp >= target:
#                 res = min(res, activePointer - passivePointer)
#                 temp -= nums[passivePointer]
#                 passivePointer +=1
            
        
#         return res if res != len(nums) + 1 else 0

# b = Solution()
# print(b.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 1:
#             return 1
#         print(len(s))
        
#         window, res = '',0

#         for c in s:
#             window = window[window.find(c)+1:]+c
#             res = max(res, len(window))

#         return res
    
# b = Solution()
# print(b.lengthOfLongestSubstring("wordgoodgoodgoodbestword"))



# from typing import List
# from collections import Counter


# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if(len(words) == 0 or len(s) == 0):
#             return []

#         wordCount = Counter(words)
#         lengthOfString = len(s)
#         countOfWords = len(words)
#         wordLength = len(words[0])
#         ans = []

#         for i in range(wordLength):
#             l = r = i
#             windowWordCounter = Counter()
#             matchedWords = 0
            
#             while r + wordLength <= lengthOfString:
#                 word = s[r:r+wordLength]
#                 r += wordLength

#                 if word not in wordCount:
#                     l=r
#                     windowWordCounter.clear()
#                     matchedWords = 0
#                     continue
                
#                 windowWordCounter[word] += 1
#                 matchedWords += 1

#                 while windowWordCounter[word] > wordCount[word]:
#                     word_to_remove = s[l:l+wordLength]
#                     l += wordLength
#                     windowWordCounter[word_to_remove] -= 1
#                     matchedWords -= 1

#                 if matchedWords == countOfWords:
#                     ans.append(l)
#         return ans

        



# b = Solution()
# print(b.findSubstring("barfoothefoobarman",["foo","bar"]))


# from collections import Counter
# import math


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # if ((len(s) < len(t)) or (len(s) == len(t) and s != t)):
#         #     return ""
        
#         # if (len(s) == len(t) and s == t) :
#         #     return s
        
#         targetChars = Counter(t)
#         minimumLength = math.inf
#         validCharCounter = 0
#         windowCounter = Counter()
#         left=0
#         minLeftPointer = -1

#         for i, c in enumerate(s):
#             windowCounter[c] += 1

#             if targetChars[c] >= windowCounter[c]:
#                 validCharCounter += 1

#             while validCharCounter == len(t) :

#                 if i - left + 1 < minimumLength:
#                     minimumLength = i - left + 1
#                     minLeftPointer = left

#                 if targetChars[s[left]] >= windowCounter[s[left]]:
#                     validCharCounter -= 1
                
#                 windowCounter[s[left]] -= 1
#                 left += 1
#         return "" if minLeftPointer < 0 else s[int(minLeftPointer):int(minLeftPointer) + minimumLength]



# b = Solution()
# print(b.minWindow("abc", "cba"))

# from typing import List

# class Solution:
    
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         row = [[False] * 9 for _ in range(9)]
#         col = [[False] * 9 for _ in range(9)]
#         subMatrix = [[False] * 9 for _ in range(9)]
#         # print(row)
#         # print(col)
#         # print(subMatrix)
#         width = 9
#         height = 9
        
#         for i in range(height):

#             for j in range(width):

#                 if board[i][j] == '.':
#                     continue

#                 num = int(board[i][j]) - 1

#                 indexOfSubMatrix = (i//3) * 3 + j//3

#                 if row[i][num] or col[j][num] or subMatrix[indexOfSubMatrix][num]:
#                     return False

#                 row[i][num] = True
#                 col[j][num] = True
#                 subMatrix[indexOfSubMatrix][num] = True
                
#         return True


# b = Solution()
# print(b.isValidSudoku([["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))

from collections import Counter
from typing import List

class Solution:

#     def traverse(self,matrix, initialY, initialX, endY, endX) :

#         if(len(matrix)//2-1 == initialY and len(matrix[0])//2-1 == initialX):
#                 return
#         if initialX < endX :
#                 print(matrix[initialY][initialX])
#                 initialX += 1
#                 self.traverse(matrix, initialY, initialX, endY, endX)
#         if initialY < endY :
#                 print(matrix[initialY][initialX])
#                 initialY += 1
#                 self.traverse(matrix,  initialY, initialX, endY, endX)
#         if initialX > 0 :
#                 print(matrix[initialY][initialX])
#                 initialX -= 1
#                 self.traverse(matrix, initialY, initialX, endY, endX)
#         if initialY > 0 :
#                 print(matrix[initialY][initialX])
#                 initialY -=1
#                 self.traverse(matrix, initialY, initialX, endY, endX)
                

    def spiralOrder(self, matrix):
      
        # Define matrix dimensions.
        rows, cols = len(matrix), len(matrix[0])
      
        # Define directions for spiral movement (right, down, left, up).
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
      
        # Initialize row and column indices and the direction index.
        row = col = direction_index = 0
      
        # Initialize the answer list and a set to keep track of visited cells.
        result = []
        visited = set()
      
        # Iterate over the cells of the matrix.
        for _ in range(rows * cols):
            # Append the current element to the result list.
            result.append(matrix[row][col])
            # Mark the current cell as visited.
            visited.add((row, col))
          
            # Calculate the next cell's position based on the current direction.
            next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]
            
        #     Check if the next cell is within bounds and not visited.
            if not (0 <= next_row < rows) or not (0 <= next_col < cols) or (next_row, next_col) in visited:
                # Change direction if out of bounds or cell is already visited.
                direction_index = (direction_index + 1) % 4
          
            # Update the row and column indices to the next cell's position.
            row += directions[direction_index][0]
            col += directions[direction_index][1]
      
        # Return the result list.
        return result
        
b=Solution()
b.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[7,8,9]])