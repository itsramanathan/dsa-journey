def is_anagram_hashmap(s, t):
    if len(s) != len(t):
            return False
        
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in t:
        if char not in count:
            return False
        else:
            count[char] -= 1
            if count[char] < 0:
                return False
    
    return True

def is_anagram_sorted(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    cases = [
        ("anagram", "nagaram", True),
        ("rat",     "car",     False),
        ("",        "",        True),
        ("a",       "ab",      False),
        ("aacc",    "ccac",    False),
        ("ab",      "ba",      True),
    ]
    
    print(f"{'Case':<25} {'Hashmap':<10} {'Sorted':<10} {'Expected':<10} {'Status'}")
    print("-" * 70)
    
    for s, t, expected in cases:
        got_h = is_anagram_hashmap(s, t)
        got_s = is_anagram_sorted(s, t)
        ok = (got_h == expected) and (got_s == expected)
        status = "✓" if ok else "✗"
        case_str = f"({s!r}, {t!r})"
        print(f"{case_str:<25} {str(got_h):<10} {str(got_s):<10} {str(expected):<10} {status}")