from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://boardgamegeek.com/")

browser.close()