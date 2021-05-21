from flask import Flask, render_template, url_for
import requests
import json
from flask import request


# Parsehub Tokens
API_KEY = "tfEZ5obab9q8"
PROJECT_TOKEN = "tnTP5mNEoTso"
RUN_TOKEN = "tG-TBhOkA99k"

# Data
response = requests.get(f'https://parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
data = json.loads(response.text)
data["states"].pop(-1)

# Making the data for graphing

# Total Case graph data state wise
graph_data = []
for i in range(len(data["states"])):
		graph_data.append((data["states"][i]["state_name"], data["states"][i]["total_cases"]))\

# Getting graph data values
labels = [row[0] for row in graph_data]
values = [row[1] for row in graph_data]

# Web app
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html", data=data, labels=labels, values=values)

@app.route("/state")
def state():
	return render_template("state.html", data=data)

@app.route("/credits")
def credits():
	return render_template("credits.html")

  
if __name__ == "__main__":
	app.run()
	