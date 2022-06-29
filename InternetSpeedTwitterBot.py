import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
USERNAME = "YOUR USERNAME"
class InternetSpeed:
    def __init__(self):
        options = Options()
        options.add_argument("--disable-save-password-bubble")
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        self.__driver = webdriver.Chrome(chrome_options=options, service=Service(ChromeDriverManager().install()))
        self._down= 0
        self.up = 0
        self.wait = WebDriverWait(self.__driver, 20)
    def get_internet_speed(self):
        self.__driver.get("https://www.speedtest.net/")
        btn_accept = self.wait.until(EC.visibility_of_element_located((By.ID,'onetrust-accept-btn-handler')))
        btn_accept.click()
        btn_go = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.start-text')))
        btn_go.click()
        while True:
            try:
                self.__driver.find_element(By.LINK_TEXT, '1')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            else:
                self._down = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.download-speed'))).text
                print(f"Down: {self._down}")
                self.up = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.upload-speed'))).text

                print(f"Up: {self.up}")
                break

    def tweet_at_provider(self):
        self.__driver.switch_to.new_window()
        self.__driver.get("https://twitter.com/i/flow/login")
        # log_in = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]/span/span')))
        # log_in.click()
        email = self.wait.until(EC.visibility_of_element_located((By.NAME, 'text')))
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)
        username = self.wait.until(EC.visibility_of_element_located((By.NAME, 'text')))
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)
        pw = self.wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        pw.send_keys(PASSWORD)
        pw.send_keys(Keys.ENTER)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main'))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[role="button"]'))).click()
        text = f"Hey internet Provider, why is my internet speed {self._down}down/{self.up}up when I pay for 100down/50up?"
        text_msg = self.__driver.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-block')
        text_msg.send_keys(text)
        tweet_btn = self.__driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')
        tweet_btn.click()



