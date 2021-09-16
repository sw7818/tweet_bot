from os import terminal_size
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from gtts import gTTS
import os
from ohbotWin import ohbot
import pandas as pd
import random
"""

Future scope of this project

1. Implement an ML model to come up with brand new jokes rather than just read them out.
2. Optimize code e.g think about weaker wifi connections
3. Get ohbot to engage more with the user more => different movements
4. Get another lip!!!



"""


ohbot.init("COM3")  # this is the com port where the robot has been detected


ohbot.reset()
driver = webdriver.Chrome(
    executable_path=r'C:\Users\swewa\chromedriver_win32\chromedriver.exe')

driver.get('https://twitter.com/notifications/mentions')

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys('Ohbot_Auto')

driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys('Curlysw88t')

driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()


time.sleep(8)
tweet0 = 'aadasdf'
tweetf = 'fish'
x = 1


def get_ans(ans):
    print(ans)
    if ans.lower() == 'yes':

        # if yes do this

        df = pd.read_csv('archive/shortjokes.csv')

        random_joke = random.randint(0, len(df))

        joke = df.iloc[random_joke, 1]

        return joke

    else:
        df = pd.read_csv('archive/shortjokes.csv')

        random_joke = random.randint(0, len(df))

        joke = df.iloc[random_joke, 1]

        return joke


def get_tweet():

    try:
        z = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span').text
    except:
        z = ''
        pass

    print('z   ' + z)

    if z == '':
        try:
            # this gets first text
            a = driver.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[1]').text
            # /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/span
        except:
            a = ''
            pass

    else:
        a = ''
    print('a   ' + a)
    try:
        # this gets first @
        b = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/span/a').text
    except:
        b = ''
        pass

    try:
        # this gets the space between the @s or the second text
        c = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[2]').text
    except:
        c = ''
        pass

    try:
        # gets the second @
        d = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/span/a').text
    except:
        d = ''
        pass

    try:
        # this gets the space between the @s or the third text
        e = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[3]').text
    except:
        e = ''
        pass

    try:
        # gets the third @
        f = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/span/a').text
    except:
        f = ''
        pass

    tweet = z + a + b + c + d + e + f

    return tweet


# so there is always going to be text first otherwise its classed as a reply.
# so in this case we assume text first
# then we find span of div 2 then text then div3 then span and so on .....
while True:

    # Rather than refreshing we want to go => all => mentions
    driver.find_element_by_xpath(
        '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[1]/a').click()
    # see above
    driver.find_element_by_xpath(
        '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
    ohbot.wait(0.6)
    ohbot.move(ohbot.EYETURN, 10)
    ohbot.wait(0.6)
    ohbot.move(ohbot.EYETURN, 0)
    ohbot.wait(0.6)
    ohbot.move(ohbot.EYETURN, 10)
    ohbot.wait(0.6)
    tweet0 = get_tweet()
    while tweet0 != tweetf:

        # Rather than refreshing we want to go => all => mentions
        driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
        time.sleep(1)

        user = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/div[1]/div[1]/span/span').text
        # need to get their username and then it'll say @joebloggs said "whatever........."
        ohbot.say(user + ',  just tweeted saying,  ' + tweet0)
        print('Oh bot said:  ' + user + ',  just tweeted saying,  ' + tweet0)

        """
        We need to add an algorithm that looks at all the tweets
        then reply to it with the question
        they will tweet at ohbot with the answer
        then ohbot responds
        the question is, in what configuration of twitter's html file will this occur
        """

        # Here we want to identify whether the user is the same

        # And what the answer is whether its yes or no if its neither keep it the same as no

        try:
            # here we are getting the username of the user to determine later on what user said what
            user0 = driver.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/div[2]/div/span').text
        except:
            pass

        if x == 1:
            # god knows what these do but i think one clicks on the reply button and the other backs up should the first one fail
            try:
                driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div').click()
            except:
                driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[4]/div/div[1]/div/div').click()

            time.sleep(2)

            # asks person if they want to hear a joke
            driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys('Would you like to hear a joke? YES or NO')

            time.sleep(1.5)
            # sends tweet
            driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()
            x = 0

        else:
            pass

        time.sleep(1)
        # Rather than refreshing we want to go => all => mentions
        driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
        time.sleep(1)

        tweet2 = get_tweet()
        print('tweet0' + tweet0)
        print('tweet2' + tweet2)

        # We check if there last tweet was the same

        if tweet0 != tweet2:
            user1 = driver.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/div[2]/div/span').text
            if user0 == user1:
                tweet3 = get_tweet()
                response = get_ans(tweet3)
                print(response)

                # i need to click on the reply button first

                try:
                    driver.find_element_by_xpath(
                        '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div').click()
                    # /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[4]/div/div[1]/div/div
                except:
                    driver.find_element_by_xpath(
                        '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[4]/div/div[1]/div/div').click()

                driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(response)  # send response back
                ohbot.say(response)
                print('Ohbot said:   ' + response)
                # i need to submit the tweet
                driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()

                tweetf = get_tweet()
                x = 1
                break
