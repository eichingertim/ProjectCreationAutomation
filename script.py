from selenium import webdriver
import os
import sys
import time


driver = webdriver.Chrome()
driver.get("https://github.com/login")


# ENTER YOUR GITHUB USERNAME
git_username = "<USERNAME>"

# ENTER YOUR GITHUB PASSWORD
git_password = "<PASSWORD>"

# ENTER THE COMPLETE PATH TO YOUR LOCATION WHERE YOU WANT TO SAVE YOUR PROJECTS
# e.g. C:/User/<USERNAME>/Documents/Projects
path = "<PATH>"



def enter_data_and_sign_in_to_gitub():

    username_field = driver.find_elements_by_xpath("//*[@id='login_field']")[0]
    username_field.send_keys(git_username)

    password_field = driver.find_elements_by_xpath("//*[@id='password']")[0]
    password_field.send_keys(git_password)

    sign_in_button = driver.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[8]")[0]
    sign_in_button.submit()



def create_new_repository(folder_name, is_public):
    title_field = driver.find_elements_by_xpath("//*[@id='repository_name']")[0]
    title_field.send_keys(folder_name)

    if (not is_public):
        print('PRIVATE')
        private_button = driver.find_elements_by_xpath("//*[@id='repository_visibility_private']")[0]
        private_button.click()

    time.sleep(1)

    create_repo_button = driver.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
    create_repo_button.click()



def create():

    folder_name = str(sys.argv[1])
    public_private = str(sys.argv[2])

    os.makedirs(path+folder_name)

    is_public = True
    if (public_private == "private"):
        print('PRIVATE')
        is_public = False

    enter_data_and_sign_in_to_gitub()
    driver.get("https://github.com/new")
    create_new_repository(folder_name, is_public)
    driver.quit()




if __name__ == "__main__":
    create()