import praw
import time
import prawcore
import random

user = '' #Bot Username
user_pass = '' #Bot Password
c_id = '' #Bot Client ID
c_secret = '' #Bot Client Secret

reddit = praw.Reddit(
    username = user,
    password = user_pass,
    client_id = c_id,
    client_secret = c_secret,
    user_agent = 'AffirmationBot by Rubix'
)

def main():

    randomTime = random.randrange(0, 24 * 3600) #Picks a random time sometime in the next 24 hours

    affirmations = ["You're looking good today!","It's going to be a great day!","WOW!","I LOVE YOU"] #This is where you input your affirmations

    pickAF = random.choice(affirmations) #Picks a random Affirmation from the list

    reddit.redditor('mc-lebowski').message('Daily Affirmation', pickAF) #Sends you that Affirmation in a PM

    print('Sleeping for random amount of time: ' + str(randomTime)) #Prints the time to console, so you can see when the next Affirmation will be sent. You can remove this line completely if you do not want to know when it will be sent.
    sleep(randomTime) #Bot sleeps for the randomly chosen amount of time

if __name__ == '__main__':
    while True:
        try:
            main()
        except BaseException:
            time.sleep(5)
