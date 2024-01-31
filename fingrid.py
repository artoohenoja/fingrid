import requests
from datetime import datetime

def convert_to_iso8601(date_str):
    try:
        # Convert the date from the given format to a datetime object
        date_object = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        
        # Convert the datetime object to ISO 8601 format
        iso8601_date = date_object.isoformat()
        
        return iso8601_date
    
    except ValueError:
        print("Invalid date format. Please check your input.")

def make_api_request(url, api_key):
    try:
        # Make a GET request adding the x-api-key header
        headers = {'x-api-key': api_key}
        response = requests.get(url, headers=headers)
        
        # Check the success of the request
        response.raise_for_status()
        
        # Print the content of the response
        print("GET request response:")
        print(response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"Error in GET request: {e}")

# Ask the user for the API key
api_key = input("Enter API key: ")

# Ask the user for the start date
start_date_str = input("Enter the start date (format e.g., 2024-02-26 12:34:56): ")

# Convert the start date to ISO 8601 format
iso8601_formatted_start_date = convert_to_iso8601(start_date_str)

# Ask the user for the end date
end_date_str = input("Enter the end date (format e.g., 2024-02-28 18:45:00): ")

# Convert the end date to ISO 8601 format
iso8601_formatted_end_date = convert_to_iso8601(end_date_str)

# Ask the user for datasetID or "list" to get the available datasetIDs
variableID = input("Enter datasetID or type 'list' to get a list of available datasetIDs: ")

if variableID.lower() == "list":
    # If variableID is "list", make a GET request and print id and nameFi
    list_url = "https://data.fingrid.fi/api/datasets?pageSize=200"
    try:
        list_response = requests.get(list_url, headers={'x-api-key': api_key})
        list_response.raise_for_status()
        list_data = list_response.json()["data"]
        
        for item in list_data:
            print(f"id: {item['id']}, nameFi: {item['nameFi']}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error in GET request for the list: {e}")

    # Ask the user for datasetID after displaying the list
    variableID = input("Enter datasetID: ")


# Form the URL and print it
url = f"https://data.fingrid.fi/api/datasets/{variableID}/data?startTime={iso8601_formatted_start_date}&endTime={iso8601_formatted_end_date}"
# print("Used URL:", url)

# Use the function for the main GET request
make_api_request(url, api_key)
