import pandas as pd
import numpy as np
import joblib


def load_fpl_data(path):
    return pd.read_csv(path)


def clean_data(df):
    df = df.dropna(subset=["player", "minutes"])
    df["minutes"] = df["minutes"].astype(float)
    return df


def generate_features(df):
    df = df.copy()

    # Simple rolling features
    df["form_3"] = df.groupby("player")["points"].rolling(3).mean().reset_index(level=0, drop=True)
    df["form_5"] = df.groupby("player")["points"].rolling(5).mean().reset_index(level=0, drop=True)

    # Attack involvement rate
    df["involvement"] = (df["goals"] + df["assists"]) / df["team_goals"].clip(lower=1)

    # Fill any gaps
    df = df.fillna(0)

    return df


def run_model_prediction(df, model_path):
    try:
        model = joblib.load(model_path)
        df["predicted_points"] = model.predict(df.select_dtypes(include=[np.number]))
    except:
        # fallback dummy model for demo
        df["predicted_points"] = (
            0.04 * df["minutes"]
            + 4 * df["xG"]
            + 3 * df["xA"]
            + 0.1 * (1 / df["opponent_strength"].clip(lower=1))
        )

    return df
