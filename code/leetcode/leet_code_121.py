def maxProfit(prices: list[int]) -> int:
    day = 0 
    for i in range(len(prices)):
        if day == i:
            pass
        else:
            if prices[day] > prices[i]:
                day = i
    highest_sell_price = prices[day]
    highest_sell_key = 0
    for i in range(len(prices)):
        if i <= day:
            pass
        else:
            if prices[i] > highest_sell_price:
                highest_sell_price = prices[i]
                highest_sell_key = i

    return highest_sell_price - prices[day] 
    


print(maxProfit([2,4,1]))