import os
import requests

GITHUB_USERNAME = "rajofearth"

def fetch_repo_details(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
    headers = {"Accept": "application/vnd.github.mercy-preview+json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        description = data.get("description", "No description available.")
        topics = data.get("topics", [])
        tags = ", ".join(topics) if topics else "general"
        return description, tags
    print(f"Failed to fetch details for {repo_name}, status code: {response.status_code}")
    return "No description available.", "general"

def fetch_readme(repo_name):
    url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{repo_name}/main/README.md"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    print(f"Failed to fetch README for {repo_name}, status code: {response.status_code}")
    return None

def create_jekyll_page(repo_name, content, description, tags):
    front_matter = f"""---
layout: projects
title: "{repo_name.replace('_', ' ').capitalize()}"
description: "{description}"
tags: [{tags}]
permalink: /projects/{repo_name}/
---
"""
    file_path = f"_projects/{repo_name}.md"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(front_matter + "\n" + content)

os.makedirs("_projects", exist_ok=True)
repos = ["rajofearth.github.io", "yplayer", "audio_file_organizer"]

for repo in repos:
    content = fetch_readme(repo)
    if content:
        description, tags = fetch_repo_details(repo)
        create_jekyll_page(repo, content, description, tags)
