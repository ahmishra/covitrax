import requests
import json

API_KEY = "tfEZ5obab9q8"
RUN_TOKEN = "te3NgbbTJRrV"
PROJECT_TOKEN = "tnTP5mNEoTso"

response = requests.get(f'https://parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
data = json.loads(response.text)


def summary():
	print(data["total"][0]["name"])
	print(data["total"][0]["values"].split()[0])

	print()

	print(data["total"][1]["name"])
	print(data["total"][1]["values"].split()[0])

	print()

	print(data["total"][2]["name"])
	print(data["total"][2]["values"].split()[0])

	print()

	print("Total Vacinated:", data["vacination"])
	print()

	print("Last Updated:", data["status"].split("[")[0], "(Data from: https://www.mohfw.gov.in/)")
	print("\n")

	for i in range(len(data["states"])):
		print("State:", data["states"][i]["state_name"])
		print("Total Cases:", data["states"][i]["total_cases"])
		print("Total Deaths:", data["states"][i]["total_deaths"])
		print("Total Cured:", data["states"][i]["total_cured"])
		print("\n")


summary()