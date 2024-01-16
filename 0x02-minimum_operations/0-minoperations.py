#!/usr/bin/python3
"""Script for minOperations function."""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    given n H characters in the file.
    """
    # editor_ops=2(Copy_All & Paste)
    # text_file_content='H'
    # given n; return min editor_ops to amount to n 'H'.
    min_num = 0
    editor_ops = 2
    if n <= 0 or not isinstance(n, int):
        return 0
    while editor_ops <= n:
        if n % editor_ops == 0:
            n = int(n / editor_ops)
            min_num += editor_ops
            editor_ops = 1
        editor_ops += 1
    return min_num
