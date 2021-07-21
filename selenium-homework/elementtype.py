from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/trickyelements.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)


def find_id():
    element1 = browser.find_element_by_id("element1")
    element2 = browser.find_element_by_id("element2")
    element3 = browser.find_element_by_id("element3")
    element4 = browser.find_element_by_id("element4")
    element5 = browser.find_element_by_id("element5")
    result = browser.find_element_by_id("result")

    element_list = [element1, element2, element3, element4, element5]
    for elem in element_list:
        if elem.tag_name == "button":
            elem.click()
            if result.text == f"{elem.text} was clicked":
                print(f"{elem.text} was clicked and text was correct")
            break


find_id()
