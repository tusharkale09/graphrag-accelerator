import requests

url = "https://cbippocjune2024.azure-api.net"
params = {
    "api-version": "2021-08-01"  # Replace with a supported version
}
headers = {
    "Ocp-Apim-Subscription-Key": "7dfdb3cfa1b340498145b91a163d7e20"
}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    print(response.json())
except requests.exceptions.HTTPError as errh:
    if response.status_code == 404:
        print("Error 404: Resource not found. Please check the URL and API version.")
    else:
        print(f"HTTP Error: {errh}")
except requests.exceptions.RequestException as err:
    print(f"Request Error: {err}")
