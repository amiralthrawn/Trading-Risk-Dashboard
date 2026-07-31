import numpy as np
import pandas as pd


def calculate_returns(data):
    return data.pct_change()


def calculate_cumulative_return(returns):
    return (1 + returns).cumprod() - 1


def calculate_volatility(returns):
    return returns.std()


def calculate_annual_volatility(returns):
    return returns.std() * np.sqrt(252)

def calculate_drawdown(price):
    """
    Calculate drawdown series.
    """
    running_max = price.cummax()
    drawdown = (price - running_max) / running_max
    return drawdown

def calculate_max_drawdown(drawdown):
    """
    Return maximum drawdown.
    """
    return drawdown.min()

def calculate_sharpe(returns):
    """
    Calculate annualized Sharpe Ratio (risk-free rate = 0).
    """
    return (returns.mean() / returns.std()) * np.sqrt(252)

def calculate_skewness(returns):
    """
    Calculate skewness.
    """
    return returns.skew()

def calculate_kurtosis(returns):
    """
    Calculate kurtosis.
    """
    return returns.kurtosis()