
def locate_smallest_window(nums):

    min_seen = float("inf");
    max_seen = -float("inf");
    left = right = None;

    for index in range(len(nums)):

        max_seen = max(nums[index],max_seen);

        if nums[index] < max_seen:
            right = index;

    for index in range(len(nums) - 1 , -1 , -1):

        min_seen = min(min_seen,nums[index]);

        if nums[index] > min_seen:
            left = index;
    return (left,right);






nums = [3,7,5,6,9];

window = locate_smallest_window(nums);

print(window);
