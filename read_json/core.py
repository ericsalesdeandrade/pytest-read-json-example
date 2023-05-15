import json


def compute_birth_year(input_data: str):
    # Parse the JSON data into a Python dictionary
    data = json.loads(input_data)

    # Compute birth year
    birth_year = 2023 - data["age"]

    return f"{data['name']} was born in {birth_year}"
