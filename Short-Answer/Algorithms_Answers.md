#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - as the size of the input increases, the runtime or space used will grow at the same rate. when n = 1, the loop iterates 1 time, when n = 2, the loop iterates 2 times, when n = 3, the loop iterates 3 times, etc. etc.

b) 
the outer loop is O(n) because as the size of the input increases, the runtime or space used grows at the same rate. if n = 1, the outer loop iterates 1 time, if n = 2, the outer loop iterates 2 times, etc. 

The second or inner loop is O(log n) because as the size of n increases, the runtime or space used wil grow at a slightly slower rate. 

However, both loops combined is polynomial O(n^c) because as the size of the input increases, the runtime or space used will grow at a faster rate. when n = 3, outer loop executes 3 times and inner loop executes 6 times (9 times), when n = 5, outer loop executes 5 times and inner loop executes 15 times (20 times).

c) O(2N) - often seen in recursive algorithms where the growth doubles with each addition to the data set. if bunnies = 5, the function executes 10 times before reaching base case. if bunnies = 10, the function executes 20 times before reaching base, etc.

## Exercise II

choose or guess a starting point or floor at or around the mid-way mark
i am now at m
drop an egg
if it breaks (oooops!)
i am too far up
retrace my steps
choose a lower floor at or around the midway mark between the ground and the middle floor
i am now at f
drop an egg
repeat this process until a floor lower than f is found
if egg is dropped from a floor and it doesn't break
a floor lower than f is found
end search and drop away!!!

the runtime complexity of this solution is O(log n) as i am using a binary search approach. the runtime or space used will grow at a slightly slower rate as the size of the input increases. 
