#!/usr/bin/env python
import requests
import json

# Constants
JSON_URL = "https://fse.studenttheses.ub.rug.nl/cgi/search/archive/advanced/export_theses_fse_JSON.js?screen=Search&dataset=archive&_action_export=1&output=JSON&exp=0%7C1%7C-date%2Fcreators_name%2Ftitle%7Carchive%7C-%7Cdegree_programme%3Adegree_programme%3AANY%3AEQ%3Acomputing_science%7C-%7Ceprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive%7Cmetadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow&n=&cache=216027"
JSON_FILE_FORMATTED = "../_data/studentprojects.json"

# Supervisor and Student filters
SUPERVISORS = [
    "Andrikopoulos", "Avgeriou", "Storm", "Capiluppi", "Rastogi", 
    "Feitosa", "Pandey", "Smedinga", "Lungu"
]

STUDENT_YEAR_PAIRS = {
    "Maingot": 2024,
    "de Haan": 2022,
    "van Ittersum": 2021,
    "Deng": 2020,
    "de Zoeten": 2020,
    "Holder": 2020,
    "Athanasakis": 2020,
    "Beuks": 2019,
    "Hertsenberg": 2019,
    "Hugenholtz": 2016,
    "Scheedler": 2016,
    "Scholtens": 2016,
    "Verbeek": 2015,
    "van Leusen": 2014,
    "Florea": 2014,
    "Lourenço": 2010,
    "Drenthen": 2009,
    "Esposito": 2009,
    "Ratelband": 2008
}

# Function to enforce title case while preserving connectors
def format_name(name):
    CONNECTORS = ["van", "de", "den", "von", "der", "la", "el", "di", "ter"]
    if not name:
        return ""

    parts = name.split()
    formatted_parts = []

    for part in parts:
        if part.lower() in CONNECTORS:
            formatted_parts.append(part.lower())
        else:
            # Handle hyphenated parts
            sub_parts = part.split('-')
            formatted_sub_parts = [sub_part.capitalize() for sub_part in sub_parts]
            formatted_parts.append('-'.join(formatted_sub_parts))

    return " ".join(formatted_parts)

# Step 1: Download the JSON file
print("Step 1: Downloading JSON data...")
response = requests.get(JSON_URL)
if response.status_code != 200:
    raise Exception(f"Failed to download JSON data: {response.status_code}")
data = response.json()

# Step 2: Filter data by supervisor or student surname and year
print("Step 2: Filtering data...")

filtered_projects = []

for project in data:
    # Check if any supervisor matches the specified surnames
    supervisors = project.get("tutors", [])
    supervisor_match = any(
        supervisor.get("name", {}).get("family") in SUPERVISORS for supervisor in supervisors
    )

    # Check if any student surname and year matches the specified pairs
    creators = project.get("creators", [])
    year = project.get("date")
    student_match = any(
        creator.get("name", {}).get("family") in STUDENT_YEAR_PAIRS and STUDENT_YEAR_PAIRS[creator.get("name", {}).get("family")] == year
        for creator in creators
    )

    # Add to filtered list if either condition matches
    if supervisor_match or student_match:
        filtered_projects.append(project)

# Step 3: Extract and format the relevant information
print("Step 3: Extracting and formatting relevant information...")

formatted_projects = []

for project in filtered_projects:
    formatted_project = {
        "title": project.get("title", ""),
        "type": project.get("thesis_type", "").replace("master", "MSc").replace("bachelor", "BSc").replace("internship_report", "Int."),
        "year": int(str(project.get("date", ""))[:4]),
        "uri": project.get("uri", ""),
        "authors": [
            {
                "name": format_name(f"{creator.get('name', {}).get('given', '')} {creator.get('name', {}).get('family', '')}").strip(),
                "email": creator.get("email", "").lower()
            }
            for creator in project.get("creators", [])
        ],
        "supervisors": [
            {
                "name": format_name(f"{supervisor.get('name', {}).get('given', '')} {supervisor.get('name', {}).get('family', '')}").strip(),
                "email": supervisor.get("email", "").lower()
            }
            for supervisor in project.get("tutors", [])
        ]
    }
    formatted_projects.append(formatted_project)

# Step 4: Write formatted data to JSON file
print("Step 4: Writing formatted data to JSON file...")
with open(JSON_FILE_FORMATTED, "w") as f:
    json.dump(formatted_projects, f, indent=2)

print(f"Script completed successfully. Output file: {JSON_FILE_FORMATTED}")
