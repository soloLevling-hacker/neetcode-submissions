'''
1. nums.sort()
Sorting takes O(n log n) time.
Why sort? It allows us to use the Two‑Pointer technique and easily skip duplicates. Without sorting, this problem is much harder.

2. for i in range(n - 2):
We fix the first number of the triplet at index i.
We only go up to n-2 because we need at least 2 more elements after i for left and right.

3. if i > 0 and nums[i] == nums[i-1]: continue
This is crucial for avoiding duplicate triplets.
Imagine nums = [-1, -1, 0, 1, 2]. If we don't skip, we'd add [-1, 0, 1] twice (using the first -1 and then the second -1).
We say: "If this number is the same as the previous one we already processed, skip it entirely."
(We don't check i > 0 to avoid nums[-1] out‑of‑bounds on the first iteration).

4. if nums[i] > 0: break
Since the array is sorted, if the smallest number we fix (nums[i]) is already greater than 0, then any three numbers starting from here will sum to more than 0 (because every subsequent number is even larger).
We can safely stop the entire loop early. This speeds things up massively.

5. target = -nums[i]
We need nums[i] + nums[left] + nums[right] == 0.
This is mathematically equivalent to finding nums[left] + nums[right] == -nums[i].
We set target = -nums[i] and now we are literally solving Two Sum II on the subarray to the right of i.

6. while left < right: (The Two‑Pointer Engine)
Exactly the same as Two Sum II!
If the sum of the two is too small → left += 1. Too big → right -= 1. Match → store the triplet.

7. Skipping duplicates for left and right (The Inner While Loops)
while left < right and nums[left] == nums[left + 1]:
    left += 1
while left < right and nums[right] == nums[right - 1]:
    right -= 1

Why do we need these?
After finding a valid triplet, let's say nums = [-2, 0, 0, 2, 2] and i=0 (value -2), left=1 (first 0), right=4 (last 2). We find [-2, 0, 2].
If we don't skip, the next iteration would move left to the second 0 and right to the first 2, giving us [-2, 0, 2] again as a duplicate.
So, we advance left past any consecutive duplicate numbers, and we move right back past any duplicate numbers.

8. left += 1 and right -= 1
After skipping duplicates, we must move both pointers one step further inward.
If we forget this, the while loop will get stuck in an infinite loop (because the sum would still equal the target, and we'd keep appending the same triplet forever).

Complexity Analysis
Time Complexity:	O(n²) – We have an outer loop (O(n)) and inside it a Two‑Pointer loop that moves across the rest of the array (O(n)). So, O(n * n) = O(n²).
Space Complexity:	O(1) or O(n) – If we ignore the space needed for the output result, we only use constant extra space (the pointers). However, sorting takes O(log n) to O(n) space depending on Python's internal Timsort. For interview purposes, we say O(1) extra space (excluding output).

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i]>0:
                break

            target = -nums[i]
            left = i + 1
            right = n - 1

            while left<right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]]) 

                    while left<right and nums[left]==nums[left+1]:
                        left += 1
                    while left<right and nums[right]==nums[right-1]:
                        right -= 1
                
                    left += 1
                    right -= 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return res