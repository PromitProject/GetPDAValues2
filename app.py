from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSV once at startup
PDAData = pd.read_csv("PDA.csv")

@app.route("/distinct/costcentertype", methods=["GET"])
def get_distinct_cost_center_type():
    distinct_values = PDAData["Cost Center Type"].dropna().unique().tolist()
    return jsonify({"Cost Center Type": distinct_values})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)