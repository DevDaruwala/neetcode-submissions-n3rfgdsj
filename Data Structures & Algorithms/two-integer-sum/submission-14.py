class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dic = {}
        for i, n in enumerate(nums):
            diff = target - n

            if diff in my_dic:
                return [my_dic[diff], i]

            my_dic[n] = i