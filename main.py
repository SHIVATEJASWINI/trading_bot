# main.py

from scripts.trading_bot import TradingBot

if __name__ == "__main__":
    bot = TradingBot(symbol='AAPL')
    bot.run()
