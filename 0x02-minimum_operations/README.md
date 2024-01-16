# Minimum Operations
This directory contains the solution to this task:
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file:
- Copy All and Paste.

Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

 - Prototype: `def minOperations(n)`
 - Returns an `integer`
 - If `n` is impossible to achieve, return `0`

- Example:
```
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```

 - Minimum number of operations: `6`
 