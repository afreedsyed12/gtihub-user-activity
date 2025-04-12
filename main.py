import requests
import os
from dotenv import load_dotenv


load_dotenv()

def fetch_github_activity(username):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GitHub token not found in environment variables.")
        return None

    url = f"https://api.github.com/users/{username}/events"
    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching GitHub activity: {response.status_code}")
        return None

def display_activity(activity):
    if not activity:
        print("No activity found or there was an error.")
        return

    for event in activity:
        print(f"{event['type']} at {event['created_at']}")
        print(f"Repository: {event['repo']['name']}")
        print(f"URL: {event['repo']['url']}\n")

def main():
    username = input("Enter the GitHub username: ")
    activity = fetch_github_activity(username)
    display_activity(activity)

if __name__ == "__main__":
    main()
