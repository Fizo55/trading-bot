from math import floor

def calculate_deviation(base_price, price):
    """
    Calculate the percent deviation from base_price to price.
    """
    return 100 * (price - base_price) / base_price

def find_pivots(prices, depth, is_high):
    """
    Find pivot points within the given prices.
    """
    for i in range(depth, len(prices) - depth):
        p = prices[i]
        max_range = prices[i - depth:i] + prices[i + 1:i + depth + 1]
        
        if is_high and all(p > x for x in max_range) or \
           not is_high and all(p < x for x in max_range):
            yield (i, p)

def zigzag(highs, lows, depth=10, deviation_threshold=5):
    """
    Calculate the ZigZag indicator based on highs and lows of price data.
    """
    data_highs = list(find_pivots(highs, floor(depth / 2), True))
    data_lows = list(find_pivots(lows, floor(depth / 2), False))

    raw_pairs = []
    last_low = (0, 0)

    for high in data_highs:
        lows = [low for low in data_lows if high[0] > low[0] > last_low[0]]
        if lows:
            last_low = lows[-1]
            if abs(calculate_deviation(last_low[1], high[1])) >= deviation_threshold:
                raw_pairs.append((high, last_low))

    # Filter out the redundant points
    filtered_pairs = []
    for i, pair in enumerate(raw_pairs):
        if not filtered_pairs or pair[1] == filtered_pairs[-1][1]:
            if pair[0][1] > filtered_pairs[-1][0][1]:
                filtered_pairs.pop()
            else:
                continue
        filtered_pairs.append(pair)

    return filtered_pairs
