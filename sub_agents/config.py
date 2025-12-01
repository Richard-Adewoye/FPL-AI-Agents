class Config:
    DATA_PATH = "data/processed/fpl_data.csv"
    MODEL_PATH = "models/fpl_model.pkl"

    # Feature window sizes
    ROLLING_WINDOWS = [3, 5]

    REQUIRED_COLUMNS = [
        "player", "team", "position",
        "minutes", "goals", "assists",
        "xG", "xA", "opponent_strength"
    ]
