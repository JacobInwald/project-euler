def is_palindrome(n: str) -> bool:
    """
    Check if a given string is palindromic.
    
    Parameters:
    n (str): The string to be checked.
    
    Returns:
    bool: True if the string is palindromic, False otherwise.
    """
    n = str(n)
    fst = n[0:len(n)//2]
    snd = n[len(n)//2+int(len(n) % 2!=0):]
    for i in range(len(fst)):
        if fst[i] != snd[-(i+1)]:
            return False
    return True


max = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if i*j > max and is_palindrome(i*j):
            max = i*j
print(max)
