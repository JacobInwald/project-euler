unit_words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
              5: 'five', 6: 'six', 7:'seven', 8: 'eight', 9: 'nine'}

teen_words = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
              14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
              18: 'eighteen', 19: 'nineteen'}

tens_words = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 
              6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

hundred = 'hundred'

thousand = 'thousand'


def numtoword(n) -> str:
    # 0-9
    for k in unit_words.keys():
        if n == k:
            return unit_words[k]
    # 10-19
    for k in teen_words.keys():
        if n == k:
            return teen_words[k]
    # tens
    for k in tens_words.keys():
        if n//10 == k:
            if n%10 != 0:
                return tens_words[k] + ' ' + numtoword(n%10)
            else:  
                return tens_words[k]
            
    if n < 100:
        return "error"
    # hundreds
    for k in unit_words.keys():
        if n//100 == k:
            if n%100 != 0:
                return unit_words[k] + ' ' + hundred + ' and ' + numtoword(n%100)
            else:  
                return unit_words[k] + ' ' + hundred
    if n < 1000:
        return "error"
    # thousands
    for k in unit_words.keys():
        if n//1000 == k:
            if n%1000 != 0:
                return unit_words[k] + ' ' + thousand + ' ' + numtoword(n%1000)
            else:  
                return unit_words[k] + ' ' + thousand
        
    return "error"

def count_letters(s):
    s=s.replace(' ', '')
    return len(s)

print(sum([count_letters(numtoword(i)) for i in range(1, 1001)]))
