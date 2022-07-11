from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

USERNAME = ""
PASSWORD = ""
PROMISED_DOWN = 100.00
PROMISED_UP = 20.00

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_drive_path = "/Users/killsamurai/Development/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_drive_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.speed_test = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        time.sleep(5)
        self.speed_test.click()
        time.sleep(60)
        self.current_down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = float(self.current_down.text)

        self.current_up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(self.current_up.text)

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.tweet_at_provider()
        else:
            print(f"Down: {self.down} \n Up: {self.up}")
            self.driver.close()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)

        #Login Code

        self.input = self.driver.find_element(By.TAG_NAME, "input")
        self.input.send_keys(USERNAME)
        self.input.send_keys(Keys.ENTER)

        time.sleep(5)

        self.password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password.click()
        self.password.send_keys(PASSWORD)
        self.password.send_keys(Keys.ENTER)

        # Tweet Code
        time.sleep(5)
        self.tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        self.tweet.click()

        time.sleep(3)

        self.text_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        self.text_box.send_keys(f" Download: {self.down}, Upload, {self.up}. Promised Download: {PROMISED_DOWN}, Promised Upload: {PROMISED_UP}")

        self.tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        self.tweet_button.click()
        time.sleep(5)
        self.driver.close()







