from InstaFollower import InstaFollower


def intro():
    INSTA_USERNAME = input("What is your instagram username? ")
    INSTA_PASSWORD = input("What is your instagram password? ")
    choice = input("Enter 'delete' to unfollow users or 'check' to check who's not following you ")

    if choice == "delete":
        print(
            "Sit back and relax, this will take a couple of minutes. Don't click anything or close the tab that pops "
            "up.")
        insta_bot = InstaFollower()
        insta_bot.return_unfollowers(INSTA_USERNAME,INSTA_PASSWORD)
        insta_bot.login(INSTA_USERNAME, INSTA_PASSWORD)
        insta_bot.unfollow(INSTA_USERNAME)
        print("Finished!")

    elif choice == "check":
        EMAIL = input("Where do you want the results emailed to? ")
        print(
            "Sit back and relax, this will take a couple of minutes. Don't click anything or close the tab that pops "
            "up.")
        insta_bot = InstaFollower()
        insta_bot.return_unfollowers(INSTA_USERNAME, INSTA_PASSWORD)
        # insta_bot.login(INSTA_USERNAME, INSTA_PASSWORD)
        # insta_bot.check_followers(INSTA_USERNAME, EMAIL)
        insta_bot.send_list(EMAIL)
        print("Finshed!")
        choice_2 = input("Would you like to unfollow all of them? Enter 'y' or 'no' ")
        if choice_2 == "y":
            insta_bot = InstaFollower()
            insta_bot.login(INSTA_USERNAME, INSTA_PASSWORD)
            insta_bot.unfollow(INSTA_USERNAME)
        else:
            print("Goodbye!")
    else:
        print("Not valid input. Try Again")
        intro()


intro()
