from .config import Config


def validate_dataset(df):
    missing = [col for col in Config.REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing columns: {missing}")

    if df.empty:
        raise ValueError("Dataset is empty.")


def validate_predictions(df):
    if "predicted_points" not in df.columns:
        raise ValueError("Predictions missing.")
    if df["predicted_points"].isnull().any():
        raise ValueError("Null predictions found.")
