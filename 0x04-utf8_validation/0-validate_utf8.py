#!/usr/bin/python3
"""Script for UTF-8 validator function."""


def validUTF8(data):
    """
        Determines if a given data set represents a valid UTF-8 encoding.
        Returns True if data is a valid UTF-8 encoding, otherwise False.
    """
    # 8-bit and 4-max-1s consts
    # Loop over data list and:
    # Extract each bit in an AND BITWISE OP = index
    # Shift index by (8-bit - 1) in a SIGNED RT SHFT(>>) OP
    # Validate utf-8 encoding pattern
    # In an inner loop(RT SHFT thro' index(bit) until 0 is encountered),
    # If char is single byte, continue to other chars in data list.
    # Sum up the consec-1s and compare it with 4-max-1s
    # Return False if consec-1s > 4-max-1s or eq to 1(Invalid utf-8)
    # Validate consec-1s
    # For multi-bytes char, check for next bytes if they start with 1
    # followed by 0
    # Return True if all the validation checks are met.

    NUMBER_OF_BITS_PER_BLOCK = 8
    MAX_NUMBER_OF_ONES = 4
    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
        if number == 0:
            index += 1
            continue
        number_of_ones = 0
        while True:
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= (NUMBER_OF_BITS_PER_BLOCK - number_of_ones - 1)
            if number == 1:
                number_of_ones += 1
            else:
                break
            if number_of_ones > MAX_NUMBER_OF_ONES:
                return False
        if number_of_ones == 1:
            return False
        index += 1
        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False
        for i in range(index, index + number_of_ones - 1):
            number = data[i]
            number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
            if number != 1:
                return False
            number >>= (NUMBER_OF_BITS_PER_BLOCK - 1)
            if number != 0:
                return False
            index += 1
    return True
