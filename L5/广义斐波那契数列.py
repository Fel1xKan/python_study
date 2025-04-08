def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        return signature[:n]

    result = signature.copy()
    while len(result) < n:
        next_num = sum(result[-3:])
        result.append(next_num)

    return result

print(tribonacci([1,1,1], 10))  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([300,200,100], 0))  # []
print(tribonacci([0.5,0.5,0.5], 30))  # 输出30个元素的列表
