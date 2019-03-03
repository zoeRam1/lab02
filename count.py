def count_char(text):
    freq = {}
    for letter in text:
        keys = freq.keys()
        if letter in keys:
            freq[letter] += 1
        else:
            freq[letter]=1
        
    for letter in freq:
        print(letter, freq[letter])
    
    return

def count_char_insensitive(text):
    return count_char(text.lower())


def count_char_ordered(text):
    
    freq = {}
    for letter in text.lower():
        keys = freq.keys()
        if letter in keys:
            freq[letter] += 1
        else:
            freq[letter]=1

    thing = sorted(freq, key = freq.get, reverse=True)
    nums = sorted(freq.values(), reverse=True)
    
    for i in range(0, len(thing)):
        print(thing[i], nums[i])
    
    return
    
    

