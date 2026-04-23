"""
Assignment 11 Success Example: API Data Fetcher

This example uses a simulated API-style JSON response so the focus remains on
response structure, selected values, and validation.
"""

import json
from pathlib import Path


def load_api_response():
    input_file = Path(__file__).with_name("11_simulated_country_response.json")

    with input_file.open("r", encoding="utf-8") as file:
        return json.load(file)


response_data = load_api_response()

print("Data source: simulated JSON response")
print("Country:", response_data["name"])
print("Region:", response_data["region"])
print("Population:", response_data["population"])
print("Capital:", response_data["capital"])

if response_data["population"] > 1000000:
    print("Population category: over one million")
else:
    print("Population category: one million or less")

