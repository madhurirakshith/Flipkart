from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/Users/Rakshith Yenadka/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("http://www.flipkart.com")
# driver.find_element_by_xpath("//a[text()='Login & Signup']").click()
# framevar=driver.find_element_by_class_name("Km0IJL col col-3-5").click()
# driver.switch_to.frame(framevar)
# print("Switch to Iframe")
driver.find_element_by_class_name("_2zrpKA").send_keys("ankiyenadka@gmail.com")
driver.find_element_by_class_name("_3v41xv").send_keys("FlipKart1123")
driver.find_element_by_class_name("_7UHT_c").click()
time.sleep(5)
driver.find_element_by_css_selector("div[class*='2PrdyR']").click()
time.sleep(5)
driver.find_element_by_xpath("//div[text()='₹39,900']").click()
cw=driver.current_window_handle
wh=driver.window_handles
for i in wh:
    if i!=cw:
        driver.switch_to.window(i)
time.sleep(5)
driver.find_element_by_xpath("//button[@class='_2AkmmA _2Npkh4 _2MWPVK']").click()
