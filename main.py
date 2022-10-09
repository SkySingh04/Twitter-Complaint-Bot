import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class SpeedBot():
    def __init__(self):
        #ENTER THE UPLOAD SPEED PROMISED BY YOUR PROVIDER
        self.Promised_Up=100.00
        #ENTER THE DOWNLOAD SPEED PROMISED BY YOUR PROVIDER
        self.Promised_Down=100.00
        #ENTER THE PATH TO YOUR CHROME DRIVER
        chrome_driver_path= r"C:\Users\User\Selenium Driver\chromedriver.exe."
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_btn = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_btn.click()
        time.sleep(45)
        download_el=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.actual_download =float(download_el.text)
        upload_el=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.actual_upload= float(upload_el.text)
        if self.actual_download<float(self.Promised_Down) or self.actual_upload< float(self.Promised_Up):
            self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        username= self.driver.find_element(By.NAME,"text")
        #ENTER YOUR USERNAME
        username.send_keys("example")
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.NAME,"password")
        #ENTER YOUR PASSWORD
        password.send_keys("1234")
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = f'''My ISP! WHY IS MY INTERNET ONLY {self.actual_download}mbps DOWN/{self.actual_upload}mbps UP
        WHEN YOU PROMISSED ME {self.Promised_Down}mbps DOWN/{self.Promised_Up}mbps UP!?!??!?!
        I WILL SUE YOUUUUUU'''
        tweet_box = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        tweet_box.send_keys(tweet)
        time.sleep(2)
        tweet_btn = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()

speed_bot= SpeedBot()
speed_bot.get_internet_speed()




