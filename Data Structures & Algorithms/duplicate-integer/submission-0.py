class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in nums:
            hmap[i] = 0
        for i in nums:
            hmap[i] += 1
        for i in hmap:
            if hmap[i] > 1:
                return True
        return False