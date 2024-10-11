import json

import requests


def fetch_data(url):
    print(f"Fetching data from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Data fetched successfully.")
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error occurred: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection error occurred: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error occurred: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


def save_data(data, filename):
    print(f"Saving data to {filename}...")
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to '{filename}'.")
    except IOError as e:
        print(f"An error occurred when writing to file: {e}")


# URLs for collections, crates, and skins
collections_url = "https://bymykel.github.io/CSGO-API/api/en/collections.json"
crates_url = "https://bymykel.github.io/CSGO-API/api/en/crates.json"
skins_url = "https://bymykel.github.io/CSGO-API/api/en/skins_not_grouped.json"

# Fetch and save collections data
collections_data = fetch_data(collections_url)
if collections_data is not None:
    save_data(collections_data, "collections.json")
else:
    print("No collections data to save.")

# Fetch and save crates data
crates_data = fetch_data(crates_url)
if crates_data is not None:
    save_data(crates_data, "crates.json")
else:
    print("No crates data to save.")

# Fetch and save skins data
skins_data = fetch_data(skins_url)
if skins_data is not None:
    save_data(skins_data, "skins.json")
else:
    print("No skins data to save.")
