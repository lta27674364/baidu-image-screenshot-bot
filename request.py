import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER_PATH = "E:/chromedownload/chromedriver-win64/chromedriver.exe"
SAVE_DIR = "real_screenshots"
os.makedirs(SAVE_DIR, exist_ok=True)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)

try:
    driver.get("https://image.baidu.com/search/index?tn=baiduimage&word=张韶涵")
    driver.implicitly_wait(10)

    for i in range(3):  # 点第1列、第2列、第3列的第一张图
        xpath = f'//*[@id="waterfall"]/ul[{i+1}]/li[1]/div/div/div[1]/a/div[1]/img'
        print(f"👉 准备点击：{xpath}")
        img = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView();", img)
        time.sleep(0.5)

        original_tabs = driver.window_handles
        img.click()
        time.sleep(1)

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > len(original_tabs))
        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(2.5)
        screenshot_path = os.path.join(SAVE_DIR, f"image_{i+1}.png")
        pyautogui.screenshot(screenshot_path)
        print(f"✅ 截图完成：{screenshot_path}")

        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])

except Exception as e:
    print("❌ 出错：", e)

finally:
    driver.quit()
