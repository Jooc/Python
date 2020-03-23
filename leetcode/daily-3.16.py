def compressString(S: str) -> str:
    begin = end = 0
    ans = ''

    while begin < len(S):
        ans += S[begin]
        num = 0
        while end < len(S) and S[end] == S[begin]:
            num += 1
            end += 1
        ans += str(num)
        begin = end
        end = begin

    if len(ans) < len(S):
        return ''.join(ans)
    return S


print(compressString('aabcccccaaa'))