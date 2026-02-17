def permutations(s):
    if s == "":
        return [""]
    
    set_1 = set()
    
    for i in range(len(s)):
        if s[i] in s[:i]:
            continue
        
        num_1 = s[:i] + s[i+1:]
        for p in permutations(num_1):
            set_1.add(s[i] + p)
    
    return sorted(list(set_1))

print(permutations("fh"))
    
