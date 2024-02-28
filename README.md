# GitLab Repository Cloning Script

This Python script allows you to clone GitLab repositories based on specific groups using the GitLab API. It supports both SSH and HTTP cloning methods.

## Prerequisites

- Python 3.x
- [Git](https://git-scm.com/)
- [GitLab API Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Remove the `.dist` extension from `credential.json.dist` file and Create a `credential.json` file with the following structure:**

   ```json
   {
     "gitlabUrl": "https://your-gitlab-instance.com",
     "privateToken": "your-gitlab-api-token",
     "apiVersion": "4",
     "cloneDirectoryPath": "/path/to/clone/directory"
   }
   ```

   Replace placeholders with your GitLab instance URL, API token, and the desired clone directory path.

## Usage

Run the script using the following command:

```bash
python main.py
```

## Options

### Cloning Mode:

- Enter `ssh` for SSH cloning.
- Enter `http` for HTTP cloning.

### Specific Group Name:

- To process all groups/repositories - Leave empty ` `
- To process a single group - `group`
- To process a sub-group - `group/sub-group`


## TO-DO
- Add `config.yml` to make it configurable
- Introduce logger service
- User input to cloning path
