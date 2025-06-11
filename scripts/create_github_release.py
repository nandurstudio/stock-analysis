import os
import requests
import base64
from pathlib import Path

def create_github_release(token, owner, repo, tag_name, name, body, files):
    """Create a GitHub release with assets"""
    # API endpoint
    api_url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    
    # Headers for authentication
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Release data
    release_data = {
        "tag_name": tag_name,
        "name": name,
        "body": body,
        "draft": False,
        "prerelease": False
    }
    
    print(f"Creating release {name}...")
    # Create the release
    response = requests.post(api_url, headers=headers, json=release_data)
    if response.status_code != 201:
        print(f"Error creating release: {response.status_code}")
        print(response.json())
        return
    
    release = response.json()
    upload_url = release["upload_url"].split("{")[0]
    
    # Upload each asset
    for file_path in files:
        file_name = os.path.basename(file_path)
        print(f"Uploading {file_name}...")
        
        with open(file_path, "rb") as f:
            content_type = "application/octet-stream"
            if file_name.endswith(".whl"):
                content_type = "application/x-wheel+zip"
            elif file_name.endswith(".tar.gz"):
                content_type = "application/gzip"
        
            headers["Content-Type"] = content_type
            params = {"name": file_name}
            data = f.read()
            
            response = requests.post(
                f"{upload_url}",
                headers=headers,
                params=params,
                data=data
            )
            
            if response.status_code != 201:
                print(f"Error uploading {file_name}: {response.status_code}")
                print(response.json())
            else:
                print(f"Successfully uploaded {file_name}")

def main():
    # Configuration
    owner = "nandurstudio"
    repo = "stock-analysis"
    tag_name = "v1.0.0"
    release_name = "PyIDX Community Stock Analysis Tool v1.0.0"
    
    # Get GitHub token from environment variable
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set")
        print("Please set your GitHub token first:")
        print('$env:GITHUB_TOKEN = "your-token-here"')
        return
    
    # Read release notes
    with open("RELEASE_NOTES.md", "r", encoding="utf-8") as f:
        release_body = f.read()
    
    # Find distribution files
    dist_dir = Path("dist")
    if not dist_dir.exists():
        print("Error: dist directory not found")
        return
    
    dist_files = [
        str(f) for f in dist_dir.glob("*")
        if f.name.endswith((".whl", ".tar.gz"))
    ]
    
    if not dist_files:
        print("Error: No distribution files found in dist/")
        return
    
    # Create the release
    create_github_release(
        token=token,
        owner=owner,
        repo=repo,
        tag_name=tag_name,
        name=release_name,
        body=release_body,
        files=dist_files
    )

if __name__ == "__main__":
    main()
