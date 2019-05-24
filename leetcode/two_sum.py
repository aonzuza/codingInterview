class Solution:
    def twoSum(self, nums,target):
        cache = {};
        for index,num in enumerate(nums):
            if num in cache:
                return [cache[num],index];
            else:
                cache[target - num] = index;
        #  nothing found
        return [0,0];


nums = [2,7,11,5];
sol = Solution();
results = sol.twoSum(nums,18);

print(results);
