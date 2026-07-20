'''
1.  The Problem in Plain English
You have a list of temperatures for 7 days. For each day, you want to know: "How many days must I wait until I see a temperature warmer than today?"
If there is no warmer day in the future, the answer is 0.

2.  The "Waiting Room" Analogy (The Secret Sauce)
Imagine we have a "Waiting Room" (this is our stack).
When a new day arrives (with its temperature), it looks into the waiting room.
The waiting room holds previous days that are still waiting to find a warmer day.
Here is the strict rule of the waiting room: The days inside are arranged so that their temperatures are always going DOWN from bottom to top. (Coldest at the bottom, hottest at the top).
When today's temperature arrives, it checks the person at the front (top) of the waiting room.
If today is hotter than that person, today is the answer for them! So they leave, and we calculate their wait time. We keep doing this until the person at the front is hotter than today (because that person is still waiting for a really hot day).


3.  Let's Watch the Code Run (Visual Dry Run)
Let's use a smaller example: temperatures = [73, 74, 75]

Day 0 (73°F):
Stack is empty, so we skip the while loop.
Push 0 onto the stack. Stack = [0]. Day 0 is waiting.

Day 1 (74°F):
stack has [0]. Check: Is 74 > 73? YES!
Pop 0. answer[0] = 1 - 0 = 1. (Day 0 waited 1 day).
Stack is empty now.
Push 1. Stack = [1]. Day 1 is waiting.

Day 2 (75°F):
stack has [1]. Check: Is 75 > 74? YES!
Pop 1. answer[1] = 2 - 1 = 1. (Day 1 waited 1 day).
Push 2. Stack = [2]. Day 2 is waiting.
Loop ends. Day 2's answer is still 0 because no one hotter came.
Result: [1, 1, 0]. Perfect!

4.  The Magic Happens (Popping MULTIPLE days)
What if today is really hot? It can answer for multiple previous days at once!

Let's use temperatures = [70, 71, 60, 72]

Day 0 (70): Stack [0]
Day 1 (71): 71 > 70? Yes. Pop 0, Ans[0]=1. Stack []. Push 1. Stack [1]
Day 2 (60): 60 > 71? No. Push 2. Stack [1, 2] (Temps: 71, 60 - decreasing)
Day 3 (72):

Check top (Day 2): Is 72 > 60? Yes. Pop Day 2. Ans[2] = 3 - 2 = 1.
Check new top (Day 1): Is 72 > 71? Yes. Pop Day 1. Ans[1] = 3 - 1 = 2.
Push Day 3. Stack [3].
Result: [1, 2, 1, 0].
Notice how Day 1 waited 2 days, and Day 2 waited 1 day. Today's heat resolved both!

5.  Complexity (Why this is fast)
Time O(n): Even though there is a while loop inside the for loop, each index is pushed into the stack once and popped once. So it processes 2n steps, which is linear time.
Space O(n): In the worst case (e.g., temperatures are [80, 70, 60, 50]), the stack will hold all the days because they keep getting colder, so we use memory equal to the input.
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev

            stack.append(i)

        return answer