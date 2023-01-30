def maxProfit(prices):
    maxPro = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                maxPro = max(maxPro, prices[j] - prices[i])
    return maxPro
