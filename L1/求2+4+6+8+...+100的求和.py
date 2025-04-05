def sum_of_evens(start, end):
    """
    计算从start到end之间所有偶数的和
    :param start: 起始值
    :param end: 结束值
    :return: 偶数和
    """
    total_sum = 0
    for num in range(start, end + 1, 2):
        total_sum += num
    return total_sum

# 计算2+4+6+8+...+100的和
result = sum_of_evens(2, 100)
print("2+4+6+8+...+100的和为:", result)
