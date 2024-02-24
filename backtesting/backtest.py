import ccxt
import pandas as pd
import zz

exchange = ccxt.binance({
    'rateLimit': 1200,
    'enableRateLimit': True,
})

btc_usdt = exchange.fetch_ohlcv('BTC/USDT', '1d', limit=365)
df = pd.DataFrame(btc_usdt, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

for (i_h, p_h),(i_l, p_l) in zz.zigzag(df['high'], df['low']):
    print(f'PEAK Index: {i_h}, price: {p_h}, VALLEY Index: {i_l}, price: {p_l}')
