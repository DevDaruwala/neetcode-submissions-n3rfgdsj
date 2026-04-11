class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #n = len(nums)
        ans = set()
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.add(nums[i])
                #print(ans)
            else:
                return True
        return False