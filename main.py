# main.py

import gitlab_operations
import config


def main():
    try:
        gitlab_username = ""
        gitlab_password = ""

        credentials = config.load_credentials()
        gl = gitlab_operations.initialize_gitlab(credentials)

        cloning_mode = input("Please select cloning mode (ssh / http): ")

        if cloning_mode == "http":
            gitlab_username = input("GitLab UserName: ")
            gitlab_password = input("GitLab Password: ")

        group_name = input("Specific Group Name (xyz / leave it empty): ")

        if group_name:
            # Get the specific group
            group = gl.groups.get(group_name)
            if group:
                print("Group Name: ", group.name)
                gitlab_operations.process_group(
                    credentials, cloning_mode, gitlab_username, gitlab_password, group
                )
            else:
                print(f"Group not found: {group_name}")
        else:
            # Get all groups
            groups = gl.groups.list()
            for group in groups:
                print("Group Name: ", group.name)
                gitlab_operations.process_group(
                    credentials, cloning_mode, gitlab_username, gitlab_password, group
                )

    except gitlab.GitlabAuthenticationError as auth_error:
        print(f"Authentication failed: {auth_error}")
    except Exception as e:
        print(f"Something Bad Happened: {e}")


if __name__ == "__main__":
    main()
