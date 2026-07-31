import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st

from src.visualization import (
    plot_cumulative_return,
    plot_drawdown,
    plot_return_distribution
)

from src.data_loader import load_market_data
from src.risk_metrics import (
    calculate_returns,
    calculate_sharpe,
    calculate_annual_volatility,
    calculate_drawdown,
    calculate_max_drawdown
)


st.set_page_config(
    page_title="Trading Risk Dashboard",
    page_icon="📈",
    layout="wide"
)


st.title("📈 Trading Risk Dashboard")


assets = {
    "Nasdaq Composite": "^IXIC",
    "Gold": "GC=F",
    "Brent Crude Oil": "BZ=F"
}

asset_name = st.selectbox(
    "Select an asset",
    list(assets.keys())
)

ticker = assets[asset_name]

data = load_market_data(
    ticker,
    "2025-01-01",
    "2026-01-01"
)


close_price = data["Close"].squeeze()

current_price = close_price.iloc[-1]


returns = calculate_returns(close_price)

total_return = (1 + returns.dropna()).prod() - 1


sharpe = calculate_sharpe(returns)

volatility = calculate_annual_volatility(returns)

drawdown = calculate_drawdown(close_price)

max_drawdown = calculate_max_drawdown(drawdown)


st.subheader("Performance Analysis")

cumulative_return = (
    1 + returns
).cumprod() - 1

st.line_chart(
    cumulative_return,
    height=400
)


st.subheader("Drawdown Analysis")

st.line_chart(drawdown)

st.subheader("Return Distribution")

st.bar_chart(
    returns.dropna()
)

st.subheader("Risk Metrics")

st.subheader(f"{asset_name} Overview")

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Current Price",
        f"{current_price:,.2f}"
    )


with col2:
    st.metric(
        "Total Return",
        f"{total_return*100:.2f}%"
    )


with col3:
    st.metric(
        "Sharpe Ratio",
        f"{sharpe:.2f}"
    )


with col4:
    st.metric(
        "Maximum Drawdown",
        f"{max_drawdown*100:.2f}%"
    )