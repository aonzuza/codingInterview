class Solution:
    def find_missing_number(self, arr):
        max_val = max(arr);
        min_val = 0;
        for val in range(max_val+1):
            if val not in arr:
                return val;

    def find_missing_number_by_formula(self,nums):
        expected_sum = (len(arr) * (len(arr) + 1)) / 2;
        actual_sum   = sum(nums);
        return expected_sum - actual_sum;

    def find_missing_number_by_bit_manipulation(self,nums):
        result = len(nums);
        for index,num in enumerate(nums):
            result = result ^ index ^ num;
        return result;


arr = [4,3,1,0];
sol = Solution();
missing_number = sol.find_missing_number_by_bit_manipulation(arr);

print(missing_number);
