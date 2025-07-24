from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import itertools
import openpyxl

#open the browser
service = Service("D:/Users/Bert/Desktop/Asus/chromedriver.exe")
driver = webdriver.Chrome(service = service)  

#go to the website and wait for the page loading
wait = WebDriverWait(driver, 5)
url = "https://demoui.asus.com/Advanced_Wireless_Content.asp"
driver.get(url)
wait.until(EC.presence_of_element_located((By.NAME, "band0_bw")))

#search for the desired elements in html
select_names = ["band0_bw", "band0_channel", "band1_bw", "band1_channel"]

#build tables for multiple options
selects = []
all_texts = []

for sel_name in select_names:
    sel_elem = wait.until(EC.presence_of_element_located((By.NAME, sel_name)))
    sel = Select(sel_elem)
    selects.append(sel)
    texts = [opt.text for opt in sel.options]
    all_texts.append(texts)

#multiple combinations
combos = itertools.product(*all_texts)

#open a workbook
wb = openpyxl.Workbook()
ws = wb.active

#name the worksheet
ws.title = "Option Combinations"

#name the headers
ws.append(["2.4GHz Bandwidth", "2.4GHz Control Channel", "5GHz Bandwidth", "5GHz Control Channel", "Internet Status"])

#fill the worksheet with different combinations and search for each internet status
for combo in combos:
    for sel, text in zip(selects, combo):
        sel.select_by_visible_text(text)
    
    #simulate the mouse hovering on the icon of internet status
    icon = driver.find_element(By.CSS_SELECTOR,"#connect_status")
    ActionChains(driver).move_to_element(icon).perform()

    wait = WebDriverWait(driver, 2)

    #fetch the internet status (connected or not)
    status = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#overDiv_table2 > tbody > tr > td > font > span")))
    status_text = status.text

    ws.append(list(combo) + [status_text])

#save the workbook and close the browser
wb.save("D:/Users/Bert/Desktop/Asus/asus_autotest.xlsx")
driver.quit()
print("Workbook Saved: asus_autotest.xlsx")