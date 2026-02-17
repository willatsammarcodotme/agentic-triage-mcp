import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GITHUB_PAT = os.getenv("GITHUB_PAT")
# Replace with your actual sandbox repository
REPO = os.getenv("SANDBOX_REPO")

ISSUES = [
    {
        "title": "CRITICAL: Database connection leaking credentials in logs",
        "body": "I found that the production logs are printing the full DB_PASSWORD. This is a massive security leak."
    },
    {
        "title": "The submit button is slightly off-center",
        "body": "On the contact page, the button is shifted 2px to the left. Looks messy."
    },
    {
        "title": "Feature Request: Add Dark Mode",
        "body": "The app is too bright at night. Can we get a dark mode toggle?"
    },
    {
        "title": "BUG: App crashes on checkout",
        "body": "Whenever I click pay, the whole site white-screens. I'm using Chrome."
    } # Note: This one lacks "Steps to Reproduce" to test the 'needs-info' rule!
]

def seed():
    headers = {"Authorization": f"token {GITHUB_PAT}", "Accept": "application/vnd.github.v3+json"}
    for issue in ISSUES:
        url = f"https://api.github.com/repos/{REPO}/issues"
        response = httpx.post(url, json=issue, headers=headers)
        if response.status_code == 201:
            print(f"✅ Created: {issue['title']}")
        else:
            print(f"❌ Failed {issue['title']}: {response.text}")

if __name__ == "__main__":
    seed()