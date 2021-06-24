from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"

URL = "https://boardgamegeek.com/"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

def find_id_if_exist(id_name):
    print("Keresés indul a megadott id-ra!")
    try:
        find_element = browser.find_element_by_id(id_name)
        print("Ez az id létezik a DOM-ban!")
    except:
        print("Nincs ilyen id a DOM-ban!")
    finally:
        print("Keresés lefutott!")

find_id_if_exist("nemletezik")

browser.quit()