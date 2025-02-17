def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_length = 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        print(char_set)

        max_length = max(max_length, right - left + 1)

    return max_length

print(lengthOfLongestSubstring("abccbb"))