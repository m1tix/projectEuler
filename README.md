# projectEuler

Python solutions for various [Project Euler](https://projecteuler.net/)
problems. So far, I've incorporated the matching HackerRank problem into all
problems. In some cases, such as [problem 23](src/p023.py), the HackerRank version
differs from the original problem so much that I simply created a new function.
Moreover, the Hackerrank version may not work out of the box and some
memoization is required for the program to pass the test cases. For example,
in [problem 39](src/p039.py) one would need to compute the results beforehand,
together with the rolling argmaxium.

For now, there is no desire to use any external packages such as numpy
to speed up computation. This may change in the future, however, if a lot of
matrix computations are necessary.

## TODO

- [ ] Testcase 10 of problem 29 in HackerRank does not work.
- [ ] HackerRank versions of 29, 32, 33, 34, 38, 40, 67.
- [ ] Benchmarking?
