# gitlab_operations.py

import os
import gitlab
import git


def initialize_gitlab(credentials):
    return gitlab.Gitlab(
        credentials["gitlabUrl"],
        private_token=credentials["privateToken"],
        api_version=credentials["apiVersion"],
    )


def clone_repository(
    cloning_mode, credentials, gitlab_username, gitlab_password, group, project
):
    repo_path = os.path.join(
        credentials["cloneDirectoryPath"],
        group.name.lower(),
        project.name.lower(),
    )

    if not os.path.exists(repo_path):
        print("Cloning repository: ", repo_path)
        if cloning_mode == "ssh" or not cloning_mode:
            git.Git(
                os.path.join(credentials["cloneDirectoryPath"], group.name.lower())
            ).clone(project.ssh_url_to_repo)
        elif cloning_mode == "http":
            git.Git(credentials["cloneDirectoryPath"]).clone(
                f'https://{gitlab_username}:{gitlab_password}@{project.http_url_to_repo.split("https://")[1]}'
            )
    else:
        print("Repository is already exists: ", project.name.lower())


def process_group(credentials, cloning_mode, gitlab_username, gitlab_password, group):
    group_path = os.path.join(credentials["cloneDirectoryPath"], group.name.lower())
    if not os.path.exists(group_path):
        os.mkdir(group_path)
    else:
        print("Directory is already exists: ", group.name.lower())

    for project in group.projects.list(iterator=True):
        clone_repository(
            cloning_mode, credentials, gitlab_username, gitlab_password, group, project
        )

    checkIfDirectoryIsEmpty = os.listdir(group_path)
    if len(checkIfDirectoryIsEmpty) == 0:
        print("Removing empty group: ", group.name.lower())
        os.rmdir(group_path)
