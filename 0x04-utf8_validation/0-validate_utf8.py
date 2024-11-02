#!/usr/bin/python3
""" 0-validate_utf8 """


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    """
    num_byte = 0
    for byte in data:
        byte &= 0xFF
        if num_byte == 0:
            if (byte >> 5) == 0b110:
                num_byte = 1
            elif (byte >> 4) == 0b1110:
                num_byte = 2
            elif (byte >> 3) == 0b11110:
                num_byte = 3
            elif (byte >> 7) == 0:
                continue
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
        num_byte -= 1
    return num_byte == 0
