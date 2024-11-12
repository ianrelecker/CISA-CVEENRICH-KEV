# https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

import requests
import json

# URL to the JSON data
url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

# Fetch the JSON data from the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON content
    data = response.json()
    for vulnerability in data['vulnerabilities']:
        cve_id = vulnerability.get('cveID')
        vendor_project = vulnerability.get('vendorProject')
        product = vulnerability.get('product')
        vulnerability_name = vulnerability.get('vulnerabilityName')
        short_description = vulnerability.get('shortDescription')
        due_date = vulnerability.get('dueDate')

    #json.dumps(data).
    # Print the parsed data (or work with it as needed)
    #print(json.dumps(data, indent=4))  # Pretty-printing the JSON
else:
    print(f"Failed to retrieve the data. Status code: {response.status_code}")
