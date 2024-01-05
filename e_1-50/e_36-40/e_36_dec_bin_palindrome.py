def isPalindromic(n: str) -> bool:
    fst = n[0:len(n)//2]
    snd = n[len(n)//2+int(len(n) % 2!=0):]
    for i in range(len(fst)):
        if fst[i] != snd[-(i+1)]:
            return False
    return True

def decimalToBinaryString(n: int) -> str:
    return str(bin(n))[2:]

print(sum(i for i in range(1,1000000) if isPalindromic(str(i)) and isPalindromic(decimalToBinaryString(i))))