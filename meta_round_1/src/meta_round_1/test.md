Here’s a more readable version of the problem statement:

---

### Problem: Night Bridge Crossing

A group of ( N ) travelers wants to cross an old, narrow bridge at night. The bridge can only support **two people at a time**. The group has only **one flashlight**, which must be used by anyone crossing. Traveler ( i ) can cross the bridge in ( S_i ) seconds when crossing alone.

Luckily, they also have a lightweight **wheelbarrow**. The rules for crossing are:
- Traveler ( i ) can cross the bridge alone in ( S_i ) seconds, either with or without the wheelbarrow.
- Two travelers ( i ) and ( j ) can cross together in ( S_i ) seconds if traveler ( j ) rides in the wheelbarrow pushed by traveler ( i ).

The flashlight must always be carried when crossing, and it can be brought back using the same rules. The goal is to determine if there is a strategy to get all travelers across the bridge within ( K ) seconds.

---

### Constraints
- ( 1 leq T leq 95 ) (Number of test cases)
- ( 1 leq N leq 1,000 ) (Number of travelers)
- ( 1 leq S_i, K leq 1,000,000,000 ) (Time to cross and maximum allowed time)

---

### Input Format
- The input begins with an integer ( T ), the number of test cases.
- Each test case starts with two integers ( N ) (number of travelers) and ( K ) (maximum allowed time to cross the bridge).
- The next ( N ) lines contain one integer each, ( S_i ), which represents the time traveler ( i ) takes to cross the bridge alone.

---

### Output Format
For each test case, print:
- `Case #i: YES` if it is possible for all travelers to cross the bridge within ( K ) seconds.
- `Case #i: NO` if it is not possible.

---

### Sample Explanation
For the first case:
- Traveler 3 carries traveler 4 across and returns alone.
- Traveler 2 carries traveler 3 across and returns alone.
- Traveler 1 carries traveler 2 across.

The total time is:  
( 5 + 5 + 2 + 2 + 1 = 15 ) seconds.

In the second case, there is no strategy that allows all travelers to cross within 4 seconds.

In the third case, both travelers can cross together exactly within the allotted 22 seconds.

---

This version maintains the integrity of the problem while breaking it down into digestible parts.