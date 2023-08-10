# Dynamic Programming

# Time Complexity - O(n * m)
# n is the number of coins
# m is the target sum
# The function loops through each coin. it then loops through each value between 
# 1 and sum for each coin that you have. Thus n * m

# Space Complexity - O(m)
# the dp array is created based on the target sum value

# This took me 18 min
def coinChange(coins, target_sum):

    dp = [0] * (target_sum + 1)
    dp[0] = 1  

    # Iterate through each coin 
    for coin in coins:
        # Update the dp array for each sum
        for i in range(coin, target_sum + 1):
            dp[i] += dp[i - coin]

    return dp[target_sum]

# Test cases
print(coinChange([2, 5, 10], 20))  # Output: 6
print(coinChange([2, 5, 10], 15))  # Output: 3
