import yfinance as yf


def load_market_data(ticker, start_date, end_date):
    """
    Download market data from Yahoo Finance.
    """

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    return data

def load_multiple_assets(tickers, start_date, end_date):
    """
    Download multiple assets from Yahoo Finance.
    """

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date
    )

    return data