# Notes

### Time Complexity (Big-O)

<image src=https://miro.medium.com/max/2928/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg>

#### O(1) = constant

- Never changes/constant
- Can be instances where you are pointing to something that exists (a variable) -> doesn't matter how big or small the variable is, if it's just a pointer (not a loop) it's still only one operation
- Not dependent on any changing input

| inputs | operations |
| ------ | ---------- |
| 1      | 1          |
| 10     | 1          |
| 20     | 1          |
| 30     | 1          |

#### O(n)

- Time grows at an equal rate of input (one-to-one/linear relationship)

| inputs | operations |
| ------ | ---------- |
| 1      | 1          |
| 10     | 10         |
| 20     | 20         |
| 30     | 30         |

#### O(n^2)

- Time grows at the number of inputs squared
- Gets bad _pretty_ fast

| inputs | operations |
| ------ | ---------- |
| 1      | 1          |
| 10     | 100        |
| 20     | 400        |
| 30     | 900        |

#### O(log(n))

| inputs | operations |
| ------ | ---------- |
| 1      | 1          |
| 10     | 2          |
| 20     | 3          |
| 30     | 4          |

#### Powers of 2

- 2 ^ 0 = 1

- 2 ^ 1 = 2

- 2 ^ 2 = 4

- 2 ^ 3 = 8

- 2 ^ 4 = 16

- 2 ^ 5 = 32

- 2 ^ 6 = 64

- 2 ^ 7 = 128

- 2 ^ 8 = 256

- 2 ^ 9 = 512

- 2 ^ 10 = 1024

#### Logs of n

- log2(1) = 0

- log2(2) = 1

- log2(4) = 2

- log2(8) = 3

- log2(16) = 4

- log2(32) = 5

- log2(64) = 6

- log2(128) = 7

- log2(256) = 8

- log2(512) = 9

- log2(1024) = 10

i.e. if you have a binary search with list of 1024 items, it can be done within 10 steps

#### Runtime for Specified Algorithms

| Algoritm       | Runtime    |
| -------------- | ---------- |
| Insertion Sort | O(n^2)     |
| Selection Sort | O(n^2)     |
| Bubble Sort    | O(n^2)     |
| Merge Sort     | O(n log n) |

#### Resources

https://wiki.python.org/moin/TimeComplexity

https://github.com/KevinOfNeu/ebooks/blob/master/Grokking%20Algorithms.pdf

https://www.youtube.com/watch?v=kS_gr2_-ws8&t=1000s
