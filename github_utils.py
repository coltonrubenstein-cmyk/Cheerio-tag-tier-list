from github import Github
import json

GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
REPO_NAME = "username/repo_name"
FILE_PATH = "players.json"

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def push_to_github(data):
    content_file = repo.get_contents(FILE_PATH)
    repo.update_file(FILE_PATH, "Update players.json", json.dumps(data, indent=2), content_file.sha)

def pull_from_github():
    try:
        content_file = repo.get_contents(FILE_PATH)
        data = json.loads(content_file.decoded_content.decode())
        return data
    except:
        return {"players": []}
