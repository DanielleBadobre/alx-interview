#!/usr/bin/python3
""" 0-validate_utf8 """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    n_bytes = 0
    first_mask = 1 << 7
    second_mask = 1 << 6
    for num in data:
        byte = num & 255
        if n_bytes == 0:
            mask = 1 << 7
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                continue
            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte starts with 10
            if not (byte & first_mask and not (byte & second_mask)):
                return False
        n_bytes -= 1
    # Check if all characters were completed
    return n_bytes == 0
