# TDD

## How to write a test

* Arrange - Instantiate the stuff that you want to test
* Act - Perform operations on that stuff
* Assert - Check that your stuff did what you expect

## Steps of TDD

There are three stages that your code should go through:

* Red -  Write a test that fails
* Green - Write the code that passes the test
* Refactor - Make the code as clean as possible

## “Laws” of TDD

* No production code that didn’t have a failing test.
* Only write the minimum required for a unit test to have any failure (including compilation)
  * Only test and code one thing at a time
  * If you can’t test a small thing, then you probably need to rethink the solution.
* Only write the minimum code needed to make the test pass
  * Only code one thing at a time.
  * If you can’t make a small solution to make a test pass, you may need to rethink the solution
  * Sliming: Write the most minimal, hard-coded, purposefully-stupid code possible to make our tests pass
