"""
HOW THIS ITERATIVE REVERSAL WORKS (Step-by-Step):

1. We create 'prev' and set it to None.
       Why? Because after reversal, the original head (node 1)
       will become the new tail, and every tail must point to None.

2. We create 'curr' and set it to 'head' (node 1).
       This is our walking pointer that moves through the list.

3. While 'curr' is not None:

    a) SAVE THE REST OF THE WORLD:
        next_temp = curr.next
        Before we break the link from 1 to 2, we store node 2 (and everything
        after it) into 'next_temp'. If we don't do this, we lose the rest of the list forever!

    b) REVERSE THE ARROW:
        curr.next = prev
        We point the current node's 'next' backward.
        Example: 1.next was pointing to 2. Now 1.next points to None (prev).
        We are replacing the "pointer to the next node" with a "pointer to the previous node".

    c) MOVE THE 'prev' ANCHOR FORWARD:
        prev = curr
        Now that node 1 is "finished" (it points backward), we make 'prev'
        equal to node 1. In the next loop, node 2 will point back to this.

    d) TACK BACK TO THE SAVED LIST AND CONTINUE:
        curr = next_temp
        We grab the saved node 2 (and the rest) back from 'next_temp' and
        set it as the new 'curr'. Now we repeat the process on node 2.

4. When 'curr' becomes None, we have processed every node.
        'prev' is now standing on the very last node (which is the new head).
        We return 'prev'.

    VISUAL TRACE FOR [1 -> 2 -> 3 -> None]:

        Loop 1 (curr=1):
          - next_temp = 2 (save node 2)
          - 1.next = None (break link to 2)
          - prev = 1
          - curr = 2
          Result: None <- 1  and  2 -> 3 -> None

        Loop 2 (curr=2):
          - next_temp = 3
          - 2.next = 1 (2 points backward to 1)
          - prev = 2
          - curr = 3
          Result: None <- 1 <- 2  and  3 -> None

        Loop 3 (curr=3):
          - next_temp = None
          - 3.next = 2 (3 points backward to 2)
          - prev = 3
          - curr = None
          Result: None <- 1 <- 2 <- 3

        Loop ends. Return prev (which is node 3).
        Final list: 3 -> 2 -> 1 -> None

The Big Revelation
When you do curr.next = prev, you are not "copying" the previous list into curr.
You are telling the new node: "Hey, your next pointer should point to THIS address (which happens to be the head of the already-reversed chain)."
Because of how pointers work, the new node 3 now owns the entire chain 2 -> 1 just by holding the memory address of node 2.
So prev is just a bookmark. It always points to the very first book in a stack. When you add a new book on top, you move the bookmark to the new cover. The bookmark doesn't hold all the books; the books are physically stacked on top of each other!

Time Complexity: O(n)
The while loop runs exactly once per node in the list.
If there are n nodes, we do a constant amount of work (save, reverse, move) for each one.
No nested loops, no recursion overhead. Linear time.

Space Complexity: O(1) (Iterative)
This is the biggest win of the iterative version.
We only created 3 variables: prev, curr, and next_temp.
These take up the exact same amount of memory whether the list has 10 nodes or 10 million nodes.
We do NOT copy the list – we just rearrange the existing pointers.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
