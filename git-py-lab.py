import os
import git
import json
import gitlab

with open("credential.json") as f:
    credentials = json.load(f)

gl = gitlab.Gitlab(
    credentials["gitlabUrl"],
    private_token=credentials["privateToken"],
    api_version=credentials["apiVersion"],
)

cloning_mode = input("Please select cloning mode (ssh / http): ")

if cloning_mode == "http":
    gitlab_username = input("GitLab UserName: ")
    gitlab_password = input("GitLab Password: ")

try:
    groups = gl.groups.list()
    for group in groups:
        print("Group Name: ", group.name)
        if not os.path.exists(
            os.path.join(credentials["cloneDirectoryPath"], group.name.lower())
        ):
            os.mkdir(
                os.path.join(credentials["cloneDirectoryPath"], group.name.lower())
            )
        else:
            print("Directory is already exists: ", group.name.lower())

        for project in group.projects.list(iterator=True):
            if not os.path.exists(
                os.path.join(
                    credentials["cloneDirectoryPath"],
                    group.name.lower(),
                    project.name.lower(),
                )
            ):
                print(
                    "Cloning repository: ",
                    os.path.join(
                        credentials["cloneDirectoryPath"],
                        group.name.lower(),
                        project.name.lower(),
                    ),
                )
                if cloning_mode == "ssh" or cloning_mode == "":
                    # SSH version
                    git.Git(
                        os.path.join(
                            credentials["cloneDirectoryPath"], group.name.lower()
                        )
                    ).clone(project.ssh_url_to_repo)
                elif cloning_mode == "http":
                    # HTTPS version
                    git.Git(credentials["cloneDirectoryPath"]).clone(
                        f'https://{gitlab_username}:{gitlab_password}@{project.http_url_to_repo.split("https://")[1]}'
                    )
            else:
                print("Repository is already exists: ", project.name.lower())

        # delete empty directory
        checkIfDirectoryIsEmpty = os.listdir(
            os.path.join(credentials["cloneDirectoryPath"], group.name.lower())
        )
        if len(checkIfDirectoryIsEmpty) == 0:
            print("Removing empty group: ", group.name.lower())
            os.rmdir(
                os.path.join(credentials["cloneDirectoryPath"], group.name.lower())
            )

except gitlab.GitlabAuthenticationError as auth_error:
    print(f"Authentication failed: {auth_error}")
except Exception as e:
    print(f"Something Bad Happened: {e}")
