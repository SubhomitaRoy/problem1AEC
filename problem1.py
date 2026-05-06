def max_cyclic_sum(s):
    s = s + s   
    n = len(s) // 2
    
    char_set = set()
    left = 0
    current_sum = 0
    max_sum = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            current_sum -= (ord(s[left]) - ord('a') + 1)
            left += 1
        
        char_set.add(s[right])
        current_sum += (ord(s[right]) - ord('a') + 1)
        
        if right - left + 1 > n:
            char_set.remove(s[left])
            current_sum -= (ord(s[left]) - ord('a') + 1)
            left += 1
        
        max_sum = max(max_sum, current_sum)
    
    return max_sum


s = "abca"
print(max_cyclic_sum(s))