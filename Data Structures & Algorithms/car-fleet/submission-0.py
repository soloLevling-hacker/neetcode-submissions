'''
1. cars = sorted(zip(position, speed), reverse=True)
zip(position, speed):
Imagine you have two lists:
position = [10, 8, 0, 5]
speed = [2, 4, 1, 3]

zip pairs them up like a zipper:
→ [(10, 2), (8, 4), (0, 1), (5, 3)]
Now each car has its (position, speed) stuck together in a little bundle (tuple).

sorted(..., reverse=True):
By default, sorted sorts by the first thing in the bundle (the position).
reverse=True means largest position first.
Why? Because the car closest to the target is at the front of the road. We want to process the road from the front to the back.
Example sorted result: [(10, 2), (8, 4), (5, 3), (0, 1)]
(Car at position 10 is closest to the finish line, so we look at it first).

2. stack = []
This is our "Fleet Tracker".
Important: The stack does NOT store cars. It stores the arrival times of the leading car of each fleet that we have discovered so far.
Example: If stack = [1.0, 7.0], it means:
The closest fleet to the target arrives at time 1.0.
The fleet behind it arrives at time 7.0.

3. for pos, spd in cars:
This is a for loop that goes through our sorted list.
pos gets the position, spd gets the speed for the current car.
Because we sorted with reverse=True, the loop looks at the closest car to the target first, then moves backward toward the starting line.

4. time = (target - pos) / spd
This calculates: "If this car were all alone on the road, how many hours (or seconds) would it take to reach the target?"
Example: Target is 12. Car is at position 10, speed 2.
time = (12 - 10) / 2 = 1.0 second. It takes 1 second to get there.

5. if not stack or time > stack[-1]:
This is the most important line. It decides if this car forms a new fleet.
not stack: This means the stack is empty. Since this is the very first car we look at (the one closest to the target), we always put it in the stack. It's our first fleet.
time > stack[-1]:
stack[-1] means "look at the top of the stack". In our loop, the top of the stack is the fleet directly ahead of the current car.
We compare: "Does this car take LONGER to reach the target than the car in front of it?"
If YES (time > stack[-1]): This means the car behind is slower than the car ahead. A slow car can never catch a faster car. So, it is stuck behind and must form its own brand new fleet. We push it onto the stack.
If NO (time <= stack[-1]): This means the car behind is faster (or exactly the same speed). Because the car ahead is slower, this faster car will eventually catch up and merge into that fleet. We do NOT push it onto the stack. We just throw it away (it's part of the fleet ahead).

6. stack.append(time)
We only run this line if the if statement above was True.
We add this car's arrival time to the stack as the new slowest fleet behind everyone else.

7. return len(stack)
After the loop finishes, every car has either been:
Pushed onto the stack (meaning it was slow enough to start a new fleet).
Ignored (meaning it merged into a fleet ahead).
The stack only contains the arrival times of the slowest cars in each fleet.
Therefore, the total number of fleets is exactly the number of items in the stack. We return len(stack).

Let's do a SUPER simple Dry Run with 3 cars
Target = 10
Car A: pos=9, speed=1 → Time = (10-9)/1 = 1.0 (Closest to target)
Car B: pos=5, speed=2 → Time = (10-5)/2 = 2.5
Car C: pos=2, speed=5 → Time = (10-2)/5 = 1.6

Sorted by position: Car A (9), then Car B (5), then Car C (2).
Step	Car	Time	Stack (Top is last) 	What happens?
1	     A	1.0	    []	                    Stack empty.Push 1.0. Stack = [1.0]
2	     B	2.5	    [1.0]	                Is 2.5 > 1.0? YES.Car B is slower than A. It can't catch up. New fleet! Push 2.5. Stack = [1.0, 2.5]
3	     C	1.6	    [1.0, 2.5]	            Look at top = 2.5 (Fleet B). Is 1.6 > 2.5? NO. Car C is faster than B. It WILL catch B. Merge! Do nothing.
Final len(stack) = 2.
(Fleet 1: Car A. Fleet 2: Car B + Car C). Perfect!

Why don't we need a "real" Stack here?
In this specific problem, we only ever compare the current car to the fleet immediately ahead of it (the top of the stack). We never need to look at the fleet behind the top.
Because of this, a full stack is overkill! But interviewers love the stack concept, so it's great to use.

Complexity
Time: O(n log n) – because we have to sort the cars by position.
Space: O(n) for the stack (or O(1) if using the optimized variable).
'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        last_time = -1.0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > last_time:
                fleets += 1
                last_time = time
        return fleets