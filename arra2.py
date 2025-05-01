def calculateprofits(arr , arr_size):
    profit = 0
    for i in range (1, arr_size):
        if arr[i]>arr[i - 1]:
          profit += arr[i] - arr[i - 1]
    return profit
prices = [45, 66, 88, 90 ,567 ,890  , 990]
print(calculateprofits(prices  , len(prices)))
