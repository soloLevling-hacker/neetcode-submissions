'''
1. num_set = set(nums)
What it does: Removes all duplicates and creates a hash table (HashSet).

Why it matters:
It gives us O(1) average-time membership lookups (in operator).
Duplicates are irrelevant here—once a number exists, counting it twice doesn't change the length of a consecutive sequence.

2. longest = 0
Initializes the tracker. If the input array is empty, the loop never runs, and we safely return 0.

3. for num in num_set:
We iterate over the unique elements in the set.
Crucial distinction: We are iterating over the set, not the original list. This guarantees we process each distinct number exactly once in the outer loop.

4. if num - 1 not in num_set:
This is the masterstroke of the algorithm.
The Logic: We ask: "Is there a number exactly one less than my current number?"
If YES (num - 1 exists), then num is not the smallest element in its consecutive family. We skip it entirely.
If NO (num - 1 does not exist), then num is the starting point of its consecutive sequence.

Why do we only process starting points?
Imagine the array [1, 2, 3, 4].
If we didn't have this check, we would calculate the length for 1 (length 4), 2 (length 3), 3 (length 2), and 4 (length 1) → that would be O(n²)!
By skipping 2, 3, 4, we process the entire sequence only once, from its very beginning.

5. Inside the if block:
current_num = num
current_length = 1
We initialize the sequence counter. Since we confirmed num is the start, the sequence length is at least 1.

6. while current_num + 1 in num_set:
Now we greedily look forward.
If num + 1 exists in the set, we move to it (current_num += 1) and increase the length.
We keep doing this until we hit a number whose successor is missing.

7. longest = max(longest, current_length)
Update the global maximum with the length of the sequence we just fully traversed.

The "Gotcha": How is this actually O(n)?
Many developers look at the while loop inside the for loop and assume it is O(n²).

Here is why it is strictly O(n):
The outer for loop visits every element in the set.
However, the inner while loop only runs for the starting elements of a sequence.
Because we skip all non-starts (due to if num - 1 in set), the total number of iterations performed across all while loops across the entire runtime is exactly n (the length of the longest sequence + length of other sequences). Every time the while increments, it consumes a unique number.

Total Work:
Outer loop: n checks (each is O(1)).
Inner loop total: n increments across the whole run (each is O(1)).
So it runs in O(n + n) = O(n).
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                current_length = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length +=1
                
                longest = max(longest, current_length)

        return longest
