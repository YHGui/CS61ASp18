def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    right_remainder, left_remainder = 0, 0
    while n > 0:
        
        right_remainder = left_remainder
        left_remainder = n % 10 
        if right_remainder == 8 and left_remainder == 8:
            return True      
        n = n // 10

    return False