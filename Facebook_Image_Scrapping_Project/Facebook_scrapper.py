from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('F:\All_Codes\Beautiful_Soap_Tutorial_Code\chromedriver.exe', chrome_options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("Username")
password.clear()
password.send_keys("Password")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!

#wait 5 seconds to allow your new page to load
time.sleep(5)
images = [] 

#itterate over both uploaded and tagged images respectively
for i in ["photos_of", "photos_by"]:
    # ************************************************
    # !! change goldie.may.750 to your own address !!
    # ************************************************
    driver.get("https://www.facebook.com/devdip.bhowmik/" + i + "/")
    time.sleep(5)
    
    #scroll down
    #increase the range to sroll more
    #example: range(0,10) scrolls down 650+ images
    for j in range(0,10 ):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

    #target all the link elements on the page
    anchors = driver.find_elements_by_tag_name('a')
    anchors = [a.get_attribute('href') for a in anchors]
    #narrow down all links to image links only
    anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
    
    print('Found ' + str(len(anchors)) + ' links to images')
    
    #extract the [1]st image element in each link
    for a in anchors:
        driver.get(a) #navigate to link
        time.sleep(5) #wait a bit
        img = driver.find_elements_by_tag_name("img")
        #print(img.__le__)
        images.append(img[0 ].get_attribute("src")) #may change in future to img[?]

print('I scraped '+ str(len(images)) + ' images!')

print( len(images) )
import os

path = os.getcwd()
path = os.path.join(path, "FB_SCRAPPER")

#create the directory
os.mkdir(path)


import wget

#download images
counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1