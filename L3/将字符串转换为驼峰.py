def to_camel_case(text):
    """
    将字符串转换为驼峰体
    :param text: 输入字符串，可能包含字母、-或_
    :return: 转换后的驼峰体字符串
    """
    # 将字符串按-或_分割成单词列表
    words = text.replace('-', ' ').replace('_', ' ').split()

    # 第一个单词保持不变，后面的单词首字母大写
    return words[0] + ''.join(word.capitalize() for word in words[1:])

# 测试用例
print(to_camel_case("the-stealth-warrior"))  # 输出 "theStealthWarrior"
print(to_camel_case("The_Stealth_Warrior"))  # 输出 "TheStealthWarrior"
print(to_camel_case("A-B-C"))               # 输出 "ABC"
