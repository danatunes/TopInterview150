
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



from typing import Counter, List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if(len(words) == 0 or len(s) == 0):
            return []

        cnt = Counter(words)
        m = len(s)
        n = len(words)
        k = len(words[0])
        i=0

        for i in range(k):
            t = 0
            l=i
            r=k
            cnt1 = 0
            while l<r:
                
        



b = Solution()
print(b.findSubstring("barfoothefoobarman",["foo","bar"]))