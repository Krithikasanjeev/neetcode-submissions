class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                start = num
                count = 1

                while start + 1 in nums_set:
                    start += 1
                    count += 1

                longest = max(longest, count)

        return longest
