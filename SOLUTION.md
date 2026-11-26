# Apple expectation

Let `b = n - m`. The process stops when at most `b` apples remain.
Let `E[k]` be the expected additional days with `k` apples remaining.
For `k <= b`, `E[k] = 0`. Otherwise, one day passes and the next remaining
count is uniformly distributed over `0, ..., k - 1`, so

`E[k] = 1 + (E[0] + ... + E[k - 1]) / k`.

Evaluate this recurrence in increasing order, maintaining the sum of
previous expectations. All transitions go to smaller states, so induction
establishes that each computed expectation, including the answer `E[n]`,
is correct. Complexity is O(n) time and O(1) auxiliary space.

Build with `make`. Run `python3 tests/verify.py ./code` to compare
all 210 valid inputs against an exact rational probability model that
propagates outcomes day by day. The sample `3 3` produces `1.83`.
