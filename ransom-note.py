def canConstruct(ransomNote: str, magazine: str) -> bool:
    msg = {}
    for c in magazine:
        msg[c] = msg.get(c, 0) + 1

    for c in ransomNote:
        if msg.get(c, 0) == 0:
            return False
        else:
            msg[c] -= 1

    return True

print(canConstruct("aa", "aaab"))