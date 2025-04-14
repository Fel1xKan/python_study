def permutations(s):
    chars = list(s)
    result = set()

    def backtrack(start):
        if start == len(chars):
            result.add(''.join(chars))
            return
        for i in range(start, len(chars)):
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]
    backtrack(0)
    return list(result)

print(permutations('abc'))
print(permutations('aba'))
print(permutations('aabb'))
print(permutations('abcd'))
print(permutations(''))
