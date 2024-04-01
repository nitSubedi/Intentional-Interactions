from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class configuredelem:
    
    def select_checkbox_by_label(self,driver, label_text):

    
        checkboxes = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".edit-fields.ui-configured-fields li"))
        )

   
        for checkbox in checkboxes:
            label_element = checkbox.find_element(By.CSS_SELECTOR, "label")
            label = label_element.get_attribute("title")
            
            if label==label_text:
                label_element.click()
                return
            

            

         





   