from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import keyboard

    
def bon_iver_at_air_studios():
    #open bon iver at air studios live session
    chrome_executable = Service(executable_path='/Users/james/chromedriver', log_path='.NUL')
    global driver
    driver = webdriver.Chrome(service=chrome_executable)
    url = "https://www.youtube.com/watch?v=A9Tp5fl18Ho"
    driver.get(url)
    #enter full screen
    keystrokes(3, "f")

def keystrokes(wait, key):
    time.sleep(wait)
    keyboard.write(key)

bon_iver_at_air_studios()