import pandas as pd


def format_player_output(pred_df):
    output = pred_df[["player", "team", "position", "predicted_points"]]
    output = output.sort_values(by="predicted_points", ascending=False)
    return output.reset_index(drop=True)


def rank_players(pred_df):
    roles = ["GK", "DEF", "MID", "FWD"]
    rankings = {}

    for r in roles:
        pos_df = pred_df[pred_df["position"] == r]
        rankings[r] = pos_df.head(5)

    return rankings
