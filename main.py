from selenium import webdriver
import pyautogui
import random
import time

from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSei_4FQwdhAXo8sF2BB76VFexk7_SYi772VOO9ghXbW-6_SJw/viewform')

for i in range(1000):
    userb = browser.find_element(By.XPATH, '//*[@id="i89"]')
    userb.click()

    submitbutton = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
    submitbutton.click()

    redobutton = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    redobutton.click()