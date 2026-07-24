'''
1. The Problem in Plain English
Imagine you have a list of numbers.
he list has n+1 numbers.
The numbers are only between 1 and n.
Because there are n+1 numbers but only n possible values (1 to n), one number must be repeated.

Example: nums = [1, 3, 4, 2, 2] (Here, n=4, numbers are 1-4, and 2 is repeated).
You have to find that repeated number without changing the array and without using extra memory (like a dictionary to count).

2. The "Magic" Trick: Treat it like a Maze / Linked List
Here is the clever idea: Treat the array indexes (0, 1, 2, 3...) as rooms, and the numbers inside as pointers to the next room.

The rule is: From room i, walk to room nums[i].
Let's do this for nums = [1, 3, 4, 2, 2]:
Start at room 0. The number is 1 → Walk to room 1.

In room 1. The number is 3 → Walk to room 3.
In room 3. The number is 2 → Walk to room 2.
In room 2. The number is 4 → Walk to room 4.
In room 4. The number is 2 → Walk to room 2.

Wait! We just came from room 2. Now we are going back to room 2!
We found a loop (cycle): 2 → 4 → 2 → 4 → 2...
Here is the golden rule: The duplicate number is always the entrance door to this loop. In this example, the loop entrance is room 2, and the duplicate number is 2.
Why? Because two different rooms (room 3 and room 4) both point to room 2. That means the number 2 appears at index 3 and index 4. That's our duplicate!

3. How do we find the entrance to the loop?
We use Floyd's Cycle Detection. Imagine two runners on a circular track:
Tortoise (Slow): Moves 1 step at a time.
Hare (Fast): Moves 2 steps at a time.
If they start running on a track that has a loop, they must eventually crash into each other inside the loop.
But crashing into each other is NOT the duplicate number. It's just some random spot inside the loop. We need the entrance to the loop. To find the entrance, we do two phases.

4. Breaking down the Code Line-by-Line
Here is the code again:

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

We start both runners at the first room (index 0).
Important: We don't move them yet; we just place them at the starting line.

Phase 1: Find the "Meeting Point" (Crash Site)
    while True:
        slow = nums[slow]         # Moves 1 step
        fast = nums[nums[fast]]   # Moves 2 steps
        if slow == fast:
            break

slow = nums[slow] means: Look at the number in your current room, and go to that room. (1 step).
fast = nums[nums[fast]] means: Look at your current room's number, go to that room, look at that room's number, and go there. (2 steps).
They keep running. Because there is a loop, eventually slow and fast will land on the same room. Let's call this room "The Crash Site".
Walkthrough for [1, 3, 4, 2, 2]:

Start: slow = 1, fast = 1.
Step 1: slow = nums[1] = 3. fast = nums[nums[1]] = nums[3] = 2. (Not equal)
Step 2: slow = nums[3] = 2. fast = nums[nums[2]] = nums[4] = 2. (EQUAL! Crash Site is room 2).

Phase 2: Find the "Entrance" (The Duplicate)
    slow = nums[0]   # Send the Tortoise back to the very start (room 0)
    while slow != fast:
        slow = nums[slow]  # Move 1 step
        fast = nums[fast]  # Move 1 step (same speed now!)
    return slow

We reset only the Tortoise back to the starting room (index 0). The Hare stays at the Crash Site.
Now, we make both move at exactly 1 step at a time.
Mathematical fact: The exact spot where they meet again is the entrance to the loop (which is our duplicate number).

Walkthrough for Phase 2:

Now: slow = nums[0] = 1. fast is still at Crash Site (room 2).
Step 1: slow = nums[1] = 3. fast = nums[2] = 4. (Not equal)
Step 2: slow = nums[3] = 2. fast = nums[4] = 2. (EQUAL! Return 2).
Boom! We found 2.
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow