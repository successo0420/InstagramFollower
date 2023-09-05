import time

import pandas as pd
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import instaloader
from EmailUser import EmailUser





def search(person, search_user):
    search_user.send_keys(Keys.CONTROL + "a")
    search_user.send_keys(Keys.DELETE)
    search_user.send_keys(person[:-2])
    time.sleep(1)
    search_user.send_keys(person[-2])
    search_user.send_keys(person[-1])

def check_difference(following, followers):
    s = set(followers)
    not_following = [x for x in following if x not in s]
    return not_following

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        self.unfollow_list = []
        
        

    def login(self, username, password):
        self.driver.get(url="https://www.instagram.com/")
        username_input = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.NAME, "username")))
        password_input = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.NAME, "password")))
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(9)

    def get_unfollowers(self,user,password):
        loader = instaloader.Instaloader()
        loader.login(user,password)
        profile = instaloader.Profile.from_username(loader.context,
                                            user)
        followees = set(profile.get_followees())
        followers = set(profile.get_followers())
        not_following = check_difference(followees,followers)
        print(not_following)
        return not_following
    
    def return_unfollowers(self, username,password):
        self.unfollow_list = self.get_unfollowers(username,password)
    
    def send_list(self,email):
        # with open("unfollow.csv", mode="w") as file:
        #     for item in not_following_list:
        #         file.write(item + "\n")
        EmailUser(self.unfollow_list, email)

    def unfollow(self, username):
        self.driver.get(f"https://www.instagram.com/{username}/following/")
        search_user = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input['
                                                                                                     '@aria-label = '
                                                                                                     '"Search input"]')))
        if self.unfollow_list is False:
            print("Unfollow List is Empty")
        else:
            for person in self.unfollow_list:
                search(person, search_user)
                time.sleep(2)
                try:
                    unfollow_btn = WebDriverWait(self.driver, 2).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "_aj1-")))
                    unfollow_btn.click()
                    confirm_btn = self.driver.find_element(By.CLASS_NAME, "_a9-_")
                    confirm_btn.click()
                    print(f"unfollowed {person}")
                except TimeoutException:
                    print(f"{person}is already unfollowed")
        
    # def get_follower_count(self):
    #     followers_count = self.driver.find_elements(By.CSS_SELECTOR, ".xieb3on")
    #     followers_count_list = [follower.text.split("\n")[1].split()[0] for follower in followers_count]
    #     user_followers = int(followers_count_list[0])
    #     return user_followers

    # def get_following_count(self):
    #     following_count = self.driver.find_elements(By.CSS_SELECTOR, ".xieb3on")
    #     following_count_list = [follower.text.split("\n")[2].split()[0] for follower in following_count]
    #     user_following = int(following_count_list[0])
    #     return user_following

    # def check_followers(self, username, email):
    #     self.driver.get(url=f"https://www.instagram.com/{username}/")
    #     time.sleep(9)
    #     current_followers = self.get_follower_count()
    #     current_following = self.get_following_count()
    #     self.driver.get(url=f"https://www.instagram.com/{username}/followers")
    #     time.sleep(9)
    #     self.scroll(current_followers / 9)
    #     followers = self.driver.find_elements(By.CSS_SELECTOR, ".xt0psk2 ._aacl")
    #     followers_link = [follower.text for follower in followers if follower != "Following" or follower != "'22 WNHS"]
    #     self.driver.get(url=f"https://www.instagram.com/{username}/following/")
    #     time.sleep(9)
    #     self.scroll(current_following / 9)
    #     following = self.driver.find_elements(By.CSS_SELECTOR, ".xt0psk2 ._aacl")
    #     following_link = [follow.text for follow in following if follow != "Follow" or follow != "'22 WNHS"]
    #     print(following_link)
    #     print(followers_link)
    #     not_following_list = check_difference(following_link, followers_link)
    #     handle_list(not_following_list, email)

    
    # def scroll(self, num):
    #     modal = self.driver.find_element(By.CSS_SELECTOR, '._aano')
    #     for i in range(round(num)):
    #         self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    #         time.sleep(3)


    # def find_followers(self, target):
    #     self.driver.get(url=f"https://www.instagram.com/{target}/followers/")
    #     time.sleep(9)

    # def follow(self):
    #     buttons = self.driver.find_elements(By.CLASS_NAME, "_acan")
    #     for button in buttons:
    #         self.actions.move_to_element(button).perform()
    #         button.click()
    #         time.sleep(1)



# def split(text):
#     parts = text.split('\n')
#     number_part = parts[1]
#     number = number_part.split()[0]

#     print(number)
#     print(parts)


# def delete_person(index):
#     try:
#         unfollow_data = pd.read_csv("unfollow.csv")
#         unfollow_data.drop(unfollow_data.index[index])
#     except FileNotFoundError:
#         print("File not created")
        

# def get_unfollow_list():
#     try:
#         with open("unfollow.csv") as file:
#             list = file.readlines()
#             list = [item.strip() for item in list]
#             return list
#     except FileNotFoundError:
#         print("File not created")


# def handle_list(not_following_list, email):
#     with open("unfollow.csv", mode="w") as file:
#         for item in not_following_list:
#             file.write(item + "\n")
#     EmailUser(not_following_list, email)
