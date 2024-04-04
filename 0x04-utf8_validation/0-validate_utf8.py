#!/usr/bin/python3
"""Module has method that determines if a given data set represents
    a valid UTF-8 encoding."""


def validUTF8(data):
    """Function."""
    def count_characters(num):
        """Function to the number of continuation bytes in a multi-byte
        UTF-8 character."""
        mask = 1 << 7
        i = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i
    i = 0
    while i < len(data):
        j = count_characters(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            check = count_characters(data[i])
            if check != 1:
                return False
            i += 1
    return True
