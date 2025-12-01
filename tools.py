# Copyright 2025 Your Name / FPL Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import os
import pandas as pd

def save_team_report_to_file(report: str, filename: str) -> dict:
    """Saves the FPL team report to a file."""
    with open(filename, "w") as f:
        f.write(report)
    return {"status": "success"}

def analyze_team_stats(directory: str) -> dict:
    """Aggregates all CSV/JSON player and fixture data from the given directory."""
    data_context = ""
    files = glob.glob(os.path.join(directory, "**"), recursive=True)
    for file in files:
        if os.path.isfile(file) and file.endswith((".csv", ".json")):
            data_context += f"\n- **{file}**:\n"
            try:
                if file.endswith(".csv"):
                    df = pd.read_csv(file)
                else:
                    df = pd.read_json(file)
                data_context += df.head(50).to_string()  # limit to first 50 rows
            except Exception as e:
                data_context += f"Error reading file: {e}"
    return {"team_data_context": data_context}
