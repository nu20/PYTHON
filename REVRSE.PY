def reverse_bits(num):
    """
    Reverses all bits in a given number.
    
    Args:
        num: The integer whose bits need to be reversed.
    
    Returns:
        The integer with reversed bits.
    """
    reversed_num = 0
    bit_count = 32  
    
    for i in range(bit_count):
        
        if num & 1:
            
            reversed_num |= 1 << (bit_count - i - 1)
        
        num >>= 1
    
    return reversed_num
number = 42  
reversed_number = reverse_bits(number)
print(f"Original number: {number}, Reversed number: {reversed_number}")