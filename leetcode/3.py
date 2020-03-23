def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    max_length = []

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j] not in s[i:j]:
                intermediate = j - i + 1
            else:
                max_length.append(j - i)
                break
            max_length.append(intermediate)

    if len(max_length) == 0:
        return len(s)

    print(max_length)
    max_length.sort(reverse=True)
    return max_length[0]


print(lengthOfLongestSubstring("aab"))
