"""Compare every valid input with exact day-by-day probability propagation."""

from fractions import Fraction
from pathlib import Path
import subprocess
import sys


executable = Path(sys.argv[1] if len(sys.argv) > 1 else "./code").resolve()
checked = 0
for n in range(1, 21):
    for m in range(1, n + 1):
        active = {n: Fraction(1)}
        expected = Fraction(0)
        for day in range(1, m + 1):
            following = {}
            for remaining, probability in active.items():
                for eaten in range(1, remaining + 1):
                    next_remaining = remaining - eaten
                    transition = probability / remaining
                    if next_remaining <= n - m:
                        expected += day * transition
                    else:
                        following[next_remaining] = (
                            following.get(next_remaining, Fraction(0)) + transition
                        )
            active = following
        assert not active
        actual = subprocess.check_output(
            [str(executable)], input=f"{n} {m}\n", text=True
        ).strip()
        wanted = f"{float(expected):.2f}"
        assert actual == wanted, (n, m, actual, wanted)
        checked += 1

print(f"Passed all {checked} valid inputs.")
