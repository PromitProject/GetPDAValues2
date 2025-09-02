from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSV once
PDAData = pd.read_csv("PDA.csv")

@app.route("/pda", methods=["POST"])
def get_pda_data():
    filters = request.json if request.is_json else {}

    # Start with full dataset
    df = PDAData.copy()

    # Apply filters progressively
    for col, val in filters.items():
        if col in df.columns:
            df = df[df[col] == val]

    # Decide next column to return
    columns = [
        "Cost Center Type",
        "Cost Center Name",
        "PS Craft",
        "Career Stage Level",
        "PS Job Title",
        "Primary Role",
        "Primary Skill"
    ]

    for col in columns:
        if col not in filters:
            distinct_values = df[col].dropna().unique().tolist()
            return jsonify({col: distinct_values})

    # If all filters applied, return final filtered record(s)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
