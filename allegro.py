from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://allegro.pl/")

driver.find_element(By.XPATH, "//*[@id='opbox-gdpr-consents-modal']/div/div[2]/div/div[2]/button[2]").send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div/div/div/div/div[3]/header/div[1]/div/div/div/form/input").send_keys("biokominki")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div/div/div/div/div[3]/header/div[1]/div/div/div/form/button").send_keys(Keys.ENTER)

links = []

for row in driver.find_elements_by_tag_name("section"):
    for art in row.find_elements_by_tag_name("article"):
        if art.get_attribute("data-analytics-view-custom-context") == "SPONSORED":
            for nag in art.find_elements_by_tag_name("h2"):
                for link in nag.find_elements_by_tag_name("a"):
                    href = link.get_attribute("href")
                    if href:
                        links.append(href)

with open("links.txt", "w") as file:
    for link in links:
        file.write(link + "\n")

for link in links:
    driver.execute_script(f"window.open('{link}', 'new_window')")
    time.sleep(1)
