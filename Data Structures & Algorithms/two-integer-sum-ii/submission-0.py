'''
Line 1: left = 0
What it does: Creates an integer variable named left and sets it to 0.
Why 0? In programming, list indices start at 0. This points to the very first element in the numbers array (the smallest number in the entire list, because the list is sorted in ascending order).
Concept: This is our "left anchor". It represents the smallest unused number we are currently considering.

Line 2: right = len(numbers) - 1
What it does: Calculates the last valid index of the list and stores it in a variable named right.

Breaking it down:
len(numbers) gives the total count of elements (e.g., 5).
- 1 adjusts it to the last index (e.g., 4).
Why? This points to the very last element in the array (the largest number).
Concept: This is our "right anchor". It represents the largest unused number we are currently considering.

Line 3: while left < right:
What it does: Starts a loop that will keep running as long as the left index is strictly smaller than the right index.
Why < and not <=?
If left equals right, that means both pointers are pointing to the exact same element in the array.
The problem asks us to find two numbers (different indices). Using the same element twice is not allowed. By stopping when they cross or meet, we guarantee we always look at two distinct elements.
Concept: This is the "search space". Initially, the search space is the entire array. Each step of the loop shrinks this space by moving one of the pointers inward.

Line 4: current_sum = numbers[left] + numbers[right]
What it does: Grabs the values currently pointed at by left and right, adds them together, and stores the result in a variable called current_sum.
Concept: This is our "test". We take the two extreme numbers available in our current search space (the smallest and the largest) and check how they add up compared to our target.

Lines 5 & 6: if current_sum == target: return [left+1, right+1]
What it does: Compares our current_sum to the target.
If they are exactly equal: We have found the winning pair!
Why left+1 and right+1?
The problem statement (LeetCode 167) explicitly asks for 1-indexed positions.
If left is 0 (first element), the problem expects us to return 1. So we add 1 to convert from 0-indexing (Python) to 1-indexing (the problem's requirement).
Concept: We immediately exit the function and hand back the answer. No further searching is needed.

Lines 7 & 8: elif current_sum < target: left += 1
What it does: If our test sum is too small (less than the target), we move the left pointer one step to the right (left += 1).
Why does this make sense? The array is sorted. If numbers[left] + numbers[right] is too small, it means the smallest number (numbers[left]) is just too tiny to pair with the current largest number (numbers[right]).
The Elimination Logic: What if we moved right instead? Moving right left would make the sum even smaller (since we'd be taking a smaller largest number). That would be going in the wrong direction! Since the sum is too small, the only way to increase it is to pick a larger small number. So, we ditch the current left value forever and move it up.
Concept: We are intelligently increasing the sum by replacing the smaller number with the next bigger one.

Lines 9 & 10: else: right -= 1
What it does: This else attaches to the elif. If the sum is neither equal nor smaller, it means it must be too large (greater than target). We move the right pointer one step to the left (right -= 1).
Why does this make sense? If numbers[left] + numbers[right] is too big, it means the largest number (numbers[right]) is too huge to pair with the current smallest number (numbers[left]).
The Elimination Logic: What if we moved left right instead? Moving left right would make the sum even larger (since we'd be taking a larger smallest number). That would increase the sum further, which is exactly what we don't want. So, we ditch the current right value forever and move it down.
Concept: We are intelligently decreasing the sum by replacing the larger number with the next smaller one.

What happens if the loop ends? (No explicit return)
If the while loop finishes without hitting the return statement, it means left and right have crossed over.
According to the problem statement, exactly one valid solution exists, so we will never actually exit the loop this way. However, if you want to be safe, you can add return [] at the very end (outside the loop) to satisfy Python's syntax.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left+1, right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

            