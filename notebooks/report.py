import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("data/features/events.csv")
    df.head()
    return (df,)


@app.cell
def _(df, plt):
    fig, ax = plt.subplots()
    ax.hist(df["duration_minutes"])
    ax.set_xlabel("Duration Minutes")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Event Durations")
    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
