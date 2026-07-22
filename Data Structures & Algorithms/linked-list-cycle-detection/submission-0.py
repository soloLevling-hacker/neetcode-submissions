'''



logic:
Start: slow = 1, fast = 1

Loop 1 Check: fast is 1, fast.next is 2 (True). Move.
slow goes: 1 → 2
fast goes: 1 → 2 → 3
Check: Is slow (2) equal to fast (3)? No.

Loop 2 Check: fast is 3, fast.next is 2 (True, because 3 points back to 2). Move.
slow goes: 2 → 3
fast goes: 3 → 2 → 3 (Because 2's next is 3).
Check: Is slow (3) equal to fast (3)? YES!
Code runs return True and the whole function stops immediately.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False