#!/usr/bin/python3
""" 0-validate_utf8 """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0
    
    # Masks for checking bytes
    first_mask = 1 << 7  # 10000000
    second_mask = 1 << 6  # 01000000
    
    for num in data:
        # Get only the 8 least significant bits
        byte = num & 255
        
        if n_bytes == 0:
            # Count number of 1s in the beginning of the byte
            mask = 1 << 7
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1
                
            # 1 byte characters
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
