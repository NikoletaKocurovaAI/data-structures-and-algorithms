"""
Three Laws of TDD (Test-Driven Development)
✔ Does the test exist before the implementation? (Ensures proper TDD flow)
✔ Does the test fail before implementation? (Prevents false positives)
✔ Does the implementation only include the necessary code to pass the test? (Avoids over-engineering)

Don't forget to check:
- Missing Type hinting
- Correct Naming conventions
- if Unit Test fixtures required
- if SetUp and TearDown required
- if Parametrized tests required
- if Context Managers required
- optimization of Time & Space complexity
- SOLID principles violation
- if Refactoring required
- if Documentation/Decision-Comment required
- if Build Operate Check pattern applied
- if Test Double or Mock Object Pattern required
- if When-Given-Then convention and/or Template Method required
- if Behavior Driven Development (extends TDD) required
- F.I.R.S.T principles violation
"""

from solution import Solution


import unittest


class SolutionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_(self) -> None:
        pass
