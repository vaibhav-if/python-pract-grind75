def longestPalindrome(s: str) -> int:
    if len(s) == 1:
        return 1
    elif s == s[::-1]:
        return len(s)

    char_map = {}
    for c in s:
        char_map[c] = char_map.get(c, 0) + 1

    if len(char_map.keys()) == 1:
        char_count = sum(char_map.values())
        return char_count

    char_count = sum([c for c in char_map.values() if c % 2 == 0])
    char_count += sum([c-1 for c in char_map.values() if c % 2 != 0])
    char_count += 1 if any(c % 2 != 0 for c in char_map.values()) else 0

    return char_count

print(longestPalindrome("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))