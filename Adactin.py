from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

serv_obj=Service("C:\\Users\\genga\\Downloads\\Chrome Driver\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://adactinhotelapp.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.NAME,"username").send_keys("Genga2503")
driver.find_element(By.NAME,"password").send_keys("KFLY08")
driver.implicitly_wait(10)
driver.find_element(By.NAME,"login").click()

drp_loc=Select(driver.find_element(By.NAME,"location")).select_by_value("Melbourne")
drp_hotel=Select(driver.find_element(By.NAME,"hotels")).select_by_value("Hotel Creek")
drp_room=Select(driver.find_element(By.NAME,"room_type")).select_by_value("Super Deluxe")
driver.find_element(By.NAME,"Submit").click()
driver.find_element(By.NAME,"radiobutton_0").click()
driver.find_element(By.NAME,"continue").click()
driver.find_element(By.NAME,"first_name").send_keys("Genga")
driver.find_element(By.NAME,"last_name").send_keys("Prabhu")
driver.find_element(By.NAME,"address").send_keys("Coimbatore")
driver.find_element(By.NAME,"cc_num").send_keys("4521658598564259")
drp_cctype=Select(driver.find_element(By.NAME,"cc_type")).select_by_value("VISA")
drp_expmonth=Select(driver.find_element(By.NAME,"cc_exp_month")).select_by_value("12")
drp_expyear=Select(driver.find_element(By.NAME,"cc_exp_year")).select_by_value("2022")
driver.find_element(By.NAME,"cc_cvv").send_keys("819")
driver.find_element(By.NAME,"book_now").click()
book_id=driver.find_element(By.XPATH,"//input[@name='order_no']").get_attribute("value")
print("Booking id is : ",book_id)


