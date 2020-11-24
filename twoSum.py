# Given a list of integers and a target value
# Write a solution that will return the INDICES of the of the two numbers used to sum to the target

# Brute Force O(n^2) complexity

class bruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for index, num in enumerate(nums):
         for other_index, other_num in enumerate(nums):
            if num + other_num == target and index != other_index:
                return [index, other_index]

# Single-pass O(n) complexity

class singlePass:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            else:
                hashMap[n] = i
