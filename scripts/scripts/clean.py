from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/events.csv")
CLEAN_PATH = Path("data/clean/events.csv")

VALID_EVENT_TYPES = {"click", "view", "purchase", "signup"}


def main():
    df = pd.read_csv(RAW_PATH)

    df = df.dropna()

    df["duration_seconds"] = pd.to_numeric(
        df["duration_seconds"],
        errors="coerce",
    )
    df = df.dropna()

    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]
    df = df[df["duration_seconds"] > 0]

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce",
        format="mixed",
    )
    df = df.dropna()

    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)


if __name__ == "__main__":
    main()