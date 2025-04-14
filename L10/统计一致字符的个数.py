def countConsistentStrings(allowed, words):
    allowed_set = set(allowed)
    count = 0
    for word in words:
        is_consistent = all(char in allowed_set for char in word)
        if is_consistent:
            count += 1

    return count

print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
