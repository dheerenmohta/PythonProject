from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in numSet:
                length = 1
                while i+length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

if __name__ == '__main__':
    print(Solution.longest_consecutive(Solution,[1,2, 100, 3, 4, 101, 103]))
