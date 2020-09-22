import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep    

while True:
    driver = webdriver.Firefox()
    driver.get("https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin")

    for _ in range(5):
        driver.execute_script("window.open('https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin');")
        sleep(0.1)
        
    sleep(3)

    for i in range(6):
        driver.switch_to.window(driver.window_handles[0])

        if driver.current_url == "https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin":
            sleep(100000)
        
        else:
            driver.close()    
    sleep(0.5)