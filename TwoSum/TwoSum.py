# -*- coding:utf-8 -*-
"""
@author: Huang Yankun
@file: TwoSum.py
@time: 2016/12/7 12:48
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(0,len(nums)-1):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([0,4,3,0],0))