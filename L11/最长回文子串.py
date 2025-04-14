def longest_palindrome(s):
    if not s:
        return 0

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_len = 1
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_len = max(max_len, len1, len2)

    return max_len

print(longest_palindrome("a"))
print(longest_palindrome("aa"))
print(longest_palindrome("baa"))
print(longest_palindrome("aab"))
print(longest_palindrome("abcdefghba"))
print(longest_palindrome("baablkj12345432133d"))
