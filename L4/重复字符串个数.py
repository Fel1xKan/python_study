def duplicate_count(text):
    """
    统计字符串中重复字符的个数
    :param text: 输入字符串，包含字母和数字
    :return: 重复字符的个数
    """
    # 将字符串转换为小写
    lower_text = text.lower()

    # 使用字典统计每个字符出现的次数
    char_count = {}
    for char in lower_text:
        char_count[char] = char_count.get(char, 0) + 1

    # 统计出现次数大于1的字符个数
    return sum(1 for count in char_count.values() if count > 1)

# 测试用例
print(duplicate_count("abcde"))          # 输出 0
print(duplicate_count("aabBcde"))        # 输出 2
print(duplicate_count("indivisibility")) # 输出 1

