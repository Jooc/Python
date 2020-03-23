import collections

def countCharacters(words: list, chars: str) -> int:
    count_chars = collections.Counter(chars)

    ans = 0
    for word in words:
        count_word = collections.Counter(word)
        for letter in count_word:
            if count_word[letter] > count_chars[letter]:
                break
        else:
            ans += len(word)

    return ans





print(countCharacters(["hello","world","leetcode"],
"welldonehoneyr"))