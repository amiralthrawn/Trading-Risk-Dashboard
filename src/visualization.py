import matplotlib.pyplot as plt
import seaborn as sns


def plot_cumulative_return(cumulative_return):

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(cumulative_return)

    ax.set_title("Cumulative Return")
    ax.set_xlabel("Date")
    ax.set_ylabel("Performance")

    ax.grid(True)

    return fig



def plot_drawdown(drawdown):

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(drawdown)

    ax.set_title("Drawdown")
    ax.set_xlabel("Date")
    ax.set_ylabel("Drawdown")

    ax.grid(True)

    return fig



def plot_return_distribution(returns):

    fig, ax = plt.subplots(figsize=(10, 4))

    sns.histplot(
        returns.dropna(),
        bins=50,
        ax=ax
    )

    ax.set_title("Return Distribution")
    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")

    return fig