import os
import sys
from github import Github

# ENTER YOUR GITHUB USERNAME
git_username = "<USERNAME>"

# ENTER YOUR GITHUB PASSWORD
git_password = "<PASSWORD>"

# ENTER THE COMPLETE PATH TO YOUR LOCATION WHERE YOU WANT TO SAVE YOUR PROJECTS
# e.g. C:/Users/<USERNAME>/Documents/Projects
path = "<PATH>"

def create_folder_and_repo():
    folder_name = str(sys.argv[1])
    public_private = str(sys.argv[2])
    os.makedirs(path+folder_name)

    user = Github(git_username, git_password).get_user()

    if (public_private == "private"):
        print('PRIVATE')
        user.create_repo(folder_name, private=True)
    else:
        print('PUBLIC')
        user.create_repo(folder_name)

    print("Succesfully created repository {}".format(folder_name))

if __name__ == "__main__":
    create_folder_and_repo()
