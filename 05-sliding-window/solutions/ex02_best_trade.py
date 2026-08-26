def max_profit(prices: list[int]) -> int:
    # Pattern: same-direction sweep where the left edge of the implicit
    # window is "lowest price seen so far". At each day, the best profit
    # ending here is today's price minus that running minimum.
    # Time: O(n). Space: O(1).
    if not prices:
        return 0

    min_so_far = prices[0]
    best = 0
    for price in prices[1:]:
        best = max(best, price - min_so_far)
        min_so_far = min(min_so_far, price)
    return best
