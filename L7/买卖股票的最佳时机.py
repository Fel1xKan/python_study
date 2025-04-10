def maxProfit(prices):
    if not prices:
        return 0

    min_price = float('inf')  # 记录最低价格
    max_profit = 0  # 记录最大利润

    for price in prices:
        # 更新最低价格
        min_price = min(min_price, price)
        # 计算当前可能的利润，并更新最大利润
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)

    return max_profit

# 测试用例
print(maxProfit([7,1,5,3,6,4]))  # 应该输出 5
print(maxProfit([7,6,4,3,1]))    # 应该输出 0
