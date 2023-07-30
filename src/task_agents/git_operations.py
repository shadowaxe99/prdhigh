```python
import git

def git_operations(repo_url, destination):
    try:
        git.Repo.clone_from(repo_url, destination)
        return {"status": "success", "message": "Repository cloned successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
```