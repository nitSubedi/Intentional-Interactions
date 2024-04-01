from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from checkboxes import configuredelem
from selenium.webdriver.common.action_chains import ActionChains
from data import student_data
from data import student_data_struct


def main():
    
    global driver, wait, service

    service = Service(executable_path='/Users/maauri/Downloads/chromedriver-mac-arm64')
    driver = webdriver.Chrome()
    #url = driver.command_executor._url
    #session_id = driver.session_id
    #driver = webdriver.Remote(command_executor=url, desired_capabilities={})

    #driver.session_id=session_id
    timeout = 10
    wait = WebDriverWait(driver, timeout)
    driver.get('https://olemiss.starrezhousing.com/StarRezWeb/campuslife/contributiondirectory#')
    driver.implicitly_wait(70)
    for key in student_data.keys():
        intentional_interaction(key,*student_data[key])
    driver.quit()


def intentional_interaction(id,description):
    
  
    add_contribution_button = driver.find_element(By.XPATH,"//button[@title='Add New']")
    add_contribution_button.click()



    description_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[14]/div[1]/section[1]/article[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]/textarea[1]")))
    description_field.send_keys(description)

    dropdown_contribution_type=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[14]/div[1]/section[1]/article[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/div[1]/div[1]/select[1]")
    dropdown1=Select(dropdown_contribution_type)
    dropdown1.select_by_visible_text("Intentional Interaction")

    time.sleep(10)


    dropdown_contribution_subtype=wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[14]/div[1]/section[1]/article[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/div[1]/div[1]/select[1]")))
    dropdown2=Select(dropdown_contribution_subtype)
    dropdown2.select_by_value("6")

    entry_field = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[14]/div[1]/section[1]/article[1]/div[1]/div[1]/div[3]/div[2]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[2]")
    entry_field.click()
    search_field = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[15]/div[1]/section[1]/article[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/input[1]")))
    search_field.send_keys(id)
    by_status = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[15]/div[1]/section[1]/article[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[1]/div[1]/div[1]/select[1]")
    dropdown3 = Select(by_status)
    dropdown3.select_by_visible_text("Student Number")
    search_entry=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[15]/div[1]/section[1]/article[1]/div[1]/div[1]/div[1]/div[2]/ul[3]/li[1]/button[1]")
    search_entry.click()



    id_element = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[15]/div[1]/section[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[2]/tbody[1]/tr[1]/td[6]")
    id_element.click()

    time.sleep(10)

    #configuredelem_instance = configuredelem()
    #configuredelem_instance.fields("Critical Thinking")
    input_text = "Intellectual Wellness"
    config_elem=configuredelem()
    config_elem.select_checkbox_by_label(driver, input_text)
    time.sleep(10)

    save_changes = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[14]/div[1]/section[1]/footer[1]/div[1]/button[1]")
    save_changes.click()
    time.sleep(10)

    #actions = ActionChains(driver)

    room_location = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[15]/div[1]/section[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[5]/div[1]/div[1]/div[2]")))
    room_location.click()
    #actions.move_to_element(room_location).click().perform()
    #room_location.click()
    room_location_filter = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[15]/div[1]/section[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[5]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")))

    room_location_filter.send_keys("Stewart")
    time.sleep(5)
    stewart = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[15]/div[1]/section[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[5]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[23]/a[1]")))
    stewart.click()
    save = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[15]/div[1]/section[1]/footer[1]/div[1]/div[1]/button[1]")
    save.click()
    time.sleep(5)

    back = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class='detail-nav-back ui-btn-close-detailscreen']")))
    back.click()
    time.sleep(5)

main()















