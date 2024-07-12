#!/usr/bin/python3
"""
This script lists 10 most recent commits of a specified GitHub repository
by a specific user.It uses the GitHub API to fetch the commit information.

Usage: python3 script_name.py <repository_name> <owner_name>

The script prints the commits in the format: <sha>: <author name>
"""

import sys
import requests


def fetch_commits(owner, repo, limit=10):
    """
    Fetch commits from a GitHub repository.

    Args:
    owner (str): The owner of the repository
    repo (str): The name of the repository
    limit (int): The maximum number of commits to fetch (default: 10)

    Returns:
    list: A list of commits, each as a tuple (sha, author_name)
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad responses

    commits = []
    for commit in response.json()[:limit]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        commits.append((sha, author_name))

    return commits


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 script_name.py <repository_name> <owner_name>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]

    try:
        commits = fetch_commits(owner, repo)
        for sha, author in commits:
            print(f"{sha}: {author}")
    except requests.RequestException as e:
        print(f"Error fetching commits: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
