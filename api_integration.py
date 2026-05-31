import requests

url = "https://api.github.com/users/octocat"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n===== GitHub User Information =====")
        print("Username:", data["login"])
        print("Name:", data["name"])
        print("Public Repositories:", data["public_repos"])
        print("Followers:", data["followers"])
        print("Following:", data["following"])

    else:
        print("Failed to fetch data.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Network Error:", e)

except ValueError:
    print("Invalid response received.")