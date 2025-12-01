from .tools import (
    load_fpl_data,
    clean_data,
    generate_features,
    run_model_prediction,
)
from .agent_utils import format_player_output, rank_players
from .validation_checkers import validate_dataset, validate_predictions


class FPLForecastAgent:
    def __init__(self, config):
        self.config = config

    def run(self):
        # Step 1: Load
        df = load_fpl_data(self.config.DATA_PATH)
        validate_dataset(df)

        # Step 2: Clean
        df = clean_data(df)

        # Step 3: Feature Engineering
        df_features = generate_features(df)

        # Step 4: Prediction
        preds = run_model_prediction(df_features, self.config.MODEL_PATH)
        validate_predictions(preds)

        # Step 5: Format Outputs
        formatted = format_player_output(preds)
        ranked = rank_players(formatted)

        return {
            "predictions": formatted,
            "rankings": ranked
        }
