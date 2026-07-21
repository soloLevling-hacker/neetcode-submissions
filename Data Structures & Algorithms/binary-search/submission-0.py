'''
Binary Search
Binary search is a classic divide-and-conquer algorithm that finds the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half, comparing the middle element with the target, and discarding the half where the target cannot lie.

How It Works
Start with two pointers: low = 0 and high = n-1 (for a 0‑indexed array of size n).

While low <= high:
Compute mid = (low + high) // 2 (or use low + (high - low) // 2 to avoid overflow).
If arr[mid] == target → return mid.
If arr[mid] < target → target lies in the right half: set low = mid + 1.
Else → target lies in the left half: set high = mid - 1.
If the loop ends, target is not present → return -1 (or an insertion point).
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1 
        return -1

