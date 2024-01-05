def isPalindromic(n: str) -> bool:
    """
    Check if a given string is palindromic.
    
    Parameters:
    n (str): The string to be checked.
    
    Returns:
    bool: True if the string is palindromic, False otherwise.
    """

    fst = n[0:len(n)//2]
    snd = n[len(n)//2+int(len(n) % 2!=0):]
    for i in range(len(fst)):
        if fst[i] != snd[-(i+1)]:
            return False
    return True

def decimalToBinaryString(n: int) -> str:
    """
    Converts a decimal number to a binary string representation.

    Args:
        n (int): The decimal number to convert.

    Returns:
        str: The binary string representation of the decimal number.
    """
    return str(bin(n))[2:]

print(sum(i for i in range(1,1000000) if isPalindromic(str(i)) and isPalindromic(decimalToBinaryString(i))))