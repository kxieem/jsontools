import json
import csv
import os
from collections.abc import MutableMapping
from datetime import datetime

def get_timestamp():
    """Generate a timestamp for file naming."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def jsonloader(filename):
    """Load JSON data from a file."""
    with open(filename, 'r') as json_file:
        return json.load(json_file)

def csvmaker(json_filename, headers=None, export_dir="output"):
    """
    Convert JSON data to a CSV file.
    - If headers are provided, only extract those.
    - If no headers are provided, dynamically extract them from the JSON.
    """
    timestamp = get_timestamp()
    os.makedirs(export_dir, exist_ok=True)

    data = jsonloader(json_filename)

    if not data:
        print("Error: JSON file is empty or invalid.")
        return

    # If headers are not provided, extract all available keys from the first entry
    if headers is None:
        headers = list({key for entry in data for key in entry.keys()})  # Get unique keys dynamically
    
    csv_filename = f"{export_dir}/extract_{timestamp}.csv"
    
    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)  # Write the selected headers

        for row in data:
            csvwriter.writerow([row.get(header, "N/A") for header in headers])

    print(f"CSV file saved: {csv_filename}")


def flatten_dict(d, parent_key='', sep='_'):
    """Recursively flattens nested dictionaries."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            if all(isinstance(i, dict) for i in v):  # If list contains dictionaries, flatten them
                for index, sub_dict in enumerate(v):
                    items.extend(flatten_dict(sub_dict, f"{new_key}_{index}", sep=sep).items())
            else:
                items.append((new_key, json.dumps(v)))  # Store lists as JSON strings
        else:
            items.append((new_key, v))
    return dict(items)

def extract_and_flatten(json_file, output_file):
    """Extracts 'data' array from JSON file, flattens it, and saves it to a new JSON file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if "data" not in data or not isinstance(data["data"], list):
        raise ValueError("Invalid JSON structure: 'data' array not found or incorrect format.")
    
    flattened_data = [flatten_dict(item) for item in data["data"]]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(flattened_data, f, indent=4, ensure_ascii=False)

    print(f"Flattened JSON saved to {output_file}")
