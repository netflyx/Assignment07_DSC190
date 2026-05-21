from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/events.csv")
CLEAN_PATH = Path("data/clean/events.csv")

VALID_EVENT_TYPES = {"click", "view", "purchase", "signup"}


def main():
    df = pd.read_csv(RAW_PATH)

    # Drop rows with missing fields
    df = df.dropna()

    # Keep only valid event types
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # Convert duration_seconds to numeric
    df["duration_seconds"] = pd.to_numeric(
        df["duration_seconds"],
        errors="coerce",
    )

    # Drop rows where duration_seconds is invalid
    df = df.dropna()

    # Keep only positive durations
    df = df[df["duration_seconds"] > 0]

    # Keep only integer-valued durations, then cast to int
    df = df[df["duration_seconds"] % 1 == 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int)

    # Parse timestamp
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce",
        format="mixed",
    )

    # Drop rows with invalid timestamps
    df = df.dropna()

    # Normalize timestamp to ISO 8601
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)


if __name__ == "__main__":
    main()