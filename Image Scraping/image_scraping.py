import os
import urllib.request
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib

PATH = "PATH TO YOUR CHROMEDRIVER"
service = Service(PATH)

querys = ["foggy view", "foggy weather", "foggy mountain"]
file_name = "foggy"

for i, query in enumerate(querys):
    driver = webdriver.Chrome(service=service)
    url = f"https://www.google.com/search?sca_esv=fb875f67547db07d&rlz=1C1ONGR_enTH1068TH1068&sxsrf=AHTn8zqyn5k_glZ4mW8xjrDNcGai5IYf5w:1740388399889&q={query}&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBjLjqIC1CYKD9D-DQAQS3Z598VAVBnbpHrmLO7c8q4i2z_8NKxsUrhjsoNgaedRpvmqVN0-mOdJGwDKTaG_DuHsb6Jl9ZgNVohdwtHQkyxkkSSoet8vY_eFcNmRS9Ffmh2nvjINwA1jw1p9kZu2V2KEcW0V-SRlzInoPeeNMhUZ6PDWh2Q&sa=X&ved=2ahUKEwifxuKC_NuLAxX7XmwGHVESL5cQtKgLegQIEBAB&biw=1745&bih=968&dpr=1.1"

    driver.get(url)
    time.sleep(5) 
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5) 

    img_results =[img for img in driver.find_elements(By.CLASS_NAME, "YQ4gaf") if int(img.get_attribute("width") or 0) > 12 and int(img.get_attribute("height") or 0) > 12]

    image_url = []
    for img in img_results :
        img_src = img.get_attribute("src")
        image_url.append(str(img_src))
        
    OUTPUT_DIR = os.path.join("imgs", file_name)
    for j, url in enumerate(image_url):
        result = os.path.join(OUTPUT_DIR, f"{file_name}{i}_{j+1}.jpg")
        urllib.request.urlretrieve(url, result)
        time.sleep(1)

    print(f"Image {j+1} downloaded successfully")
        
    driver.quit()
