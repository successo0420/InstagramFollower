import smtplib
import os

password = os.environ.get("PASSWORD")
my_email = os.environ.get("EMAIL")


class EmailUser:
    def __init__(self, not_following, email):
        message = f"Here are a list of people who you currently follow, but they do not follow you! {not_following}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Instagram Not Following Back "
                                                                        f"List!\n\n{message}")
            print(f"Successfully Sent to {email}")
