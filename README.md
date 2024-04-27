# projectEuler

Python solutions for various [Project Euler](https://projecteuler.net/)
problems. So far, I've incorporated the matching HackerRank problem into
(almost) all problems. In some cases, such as [problem 23](src/p023.py), the
HackerRank version differs from the original problem so much that I simply
created a new function. Moreover, the Hackerrank version may not work out of
the box and some memoization is required for the program to pass the test cases.
For example, in [problem 39](src/p039.py) one would need to compute the results beforehand,
together with the rolling argmaximum. Some problems were also done by hand, in
which case the exact approach is detailed in the function description.

For now, there is no desire to use any external packages such as numpy
to speed up computation. This may change in the future, however, if a lot of
matrix computations are necessary.

## Favorite problems

- [Problem 66](src/p066.py): amounts to solving a handful of pell equations. As
  such, the problem can be easily solved by using algebraic number
  theory.

## TODO

- [ ] Testcase 10 of problem 29 in HackerRank does not work.
- [ ] Few testcases of problem 50 in HackerRank do not work (inefficient?)
- [ ] HackerRank versions of 29, 32, 33, 34, 38, 47, 48, 49, 52, 67.
- [ ] Benchmarking?
