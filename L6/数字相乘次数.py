def persistence(num):
    # 如果是个位数，返回0
    if num < 10:
        return 0

    # 将数字转为字符串，方便分离各个位数
    num_str = str(num)
    count = 0

    # 当数字不是个位数时，继续计算
    while len(num_str) > 1:
        # 计算各位数字的乘积
        result = 1
        for digit in num_str:
            result *= int(digit)

        # 更新数字和计数器
        num_str = str(result)
        count += 1

    return count

# 测试用例
if __name__ == '__main__':
    print(persistence(39))  # 应该输出 3
    print(persistence(999)) # 应该输出 4
    print(persistence(4))   # 应该输出 0
    print(persistence(25))  # 应该输出 2
