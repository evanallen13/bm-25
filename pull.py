import os
import subprocess
import requests
import time
import sys

def clone_or_update_github_docs(target_dir, repo_url):
    if os.path.exists(target_dir):
        print(f"Repository already cloned in '{target_dir}'. Pulling latest changes...")
        try:
            result = subprocess.run(
                ["git", "-C", target_dir, "pull"],
                check=True, capture_output=True, text=True
            )

            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error pulling latest changes: {e}")
            print(f"Error details: {e.stderr}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
    else:
        print("Cloning GitHub docs repository...")
        try:
            result = subprocess.run(
                [
                    "git",
                    "clone",
                    "--depth=1",
                    "--single-branch",
                    "--branch", "main",
                    repo_url,
                    target_dir,
                ],
                check=True, capture_output=True, text=True
            )
            print(f"Repository cloned successfully to '{target_dir}' directory!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            print(f"Error details: {e.stderr}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False


def copy_md_files(src_dir, dest_dir):

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.md') and file not in ['index.md', 'README.md']:
                relative_path = os.path.relpath(root, src_dir)
                dest_subdir = os.path.join(dest_dir, relative_path)
                full_path = relative_path + "/" + file
                                    
                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)
                
                if os.path.exists(dest_subdir + "/" + file):
                    print(f"File already exists: {file} in {dest_subdir}, skipping fetch.")
                    continue
                
                api = "https://docs.github.com/api/article/body?pathname=/en/" + full_path.replace('.md', '')
                
                result = requests.get(api)
                time.sleep(2)
                if result.status_code == 429:
                    print("Rate limit exceeded. Please try again later.")
                    sys.exit(1)
                if result.status_code == 200:
                    with open(os.path.join(dest_subdir, file), 'w', encoding='utf-8') as f:
                        f.write(result.text)
                    print(f"Fetched and wrote: {full_path}")

def git_helper():
    repo_url = "https://github.com/github/docs.git"
    target_dir = "gh_docs"
    result = clone_or_update_github_docs(target_dir, repo_url)
    copy_md_files(f'{target_dir}/content', 'data')
    
if __name__ == "__main__":
    git_helper()