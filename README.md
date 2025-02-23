# jsontools  
## A Python utility for flattening JSON and converting JSON to CSV  

---

## Overview
`jsontools` is a lightweight Python module designed to:  
- Flatten deeply nested JSON into a flat structure  
- Extract specific fields from JSON for CSV conversion  
- Dynamically detect headers for maximum flexibility  

---

## Installation
Clone this repository:  
`git clone https://github.com/kxieem/jsontools.git
`

Then, import it into your Python script:
`from jsontools import extract_and_flatten, csvmaker
`

# Functions & Usage
Flatten Nested JSON
`from jsontools import extract_and_flatten`

# Convert nested JSON to a flat structure
`extract_and_flatten("input.json", "flattened_output.json")`
- Reads input.json
- Extracts the data array
- Flattens all nested dictionaries & lists
- Saves formatted JSON to flattened_output.json

# Convert JSON to CSV
`from jsontools import csvmaker

# Convert JSON to CSV with selected headers
`csvmaker("flattened_output.json", ["field1", "field2", "field3"])`
- Reads flattened_output.json
- Extracts only specified fields
- Saves structured CSV output in output/ directory
- If no headers are provided, csvmaker() extracts all available keys dynamically.

# Example
Input JSON (input.json)
`{
    "data": [
        {
            "user": {
                "name": "Alice",
                "id": 123
            },
            "details": {
                "age": 25,
                "city": "New York"
            }
        }
    ]
}
`

Flattened Output (flattened_output.json)
`[
    {
        "user_name": "Alice",
        "user_id": 123,
        "details_age": 25,
        "details_city": "New York"
    }
]
`
Final CSV (output/extract_YYYY-MM-DD_HH-MM-SS.csv)

# Why Use jsontools?
- Handles deeply nested JSON effortlessly
- Extracts only relevant fields for CSV
- Automatically detects missing fields
- Lightweight and reusable across projects
