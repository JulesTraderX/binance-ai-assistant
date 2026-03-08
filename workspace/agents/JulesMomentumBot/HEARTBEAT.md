# HEARTBEAT.md — JulesMomentumBot

## Every 5-minute check sequence:

1. Check USDT spot balance (spot skill)
2. Get current price: BTCUSDT
3. Get current price: ETHUSDT
4. Get RSI(14), EMA(50), EMA(200) on 1h timeframe (trading-signal skill)
5. Check volume rank for BTCUSDT and ETHUSDT (crypto-market-rank skill — must be top 10)
6. Evaluate BUY/SELL signals per SOUL.md rules
7. If signal: execute trade (max 10% USDT balance, max 2 open positions)
8. Send Telegram summary: timestamp, decision, reason, price, P&L (even if no trade)
9. On any error: retry ×2, then alert Henri on Telegram immediately
