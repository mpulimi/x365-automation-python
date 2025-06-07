import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException

def load_config():
    with open('appsettings.json') as f:
        return json.load(f)['AppSettings']

def run_once():
    config = load_config()
    print("Config loaded...")
    login_url = config["LoginUrl"]
    action_url = config["ActionUrl"]
    email = config["email"]
    password = config["password"]
    close_popups = config["closePopups"]
    print("Config variables initialized...")
    options = Options()
    #options.add_argument("--headless=new")
    #options.add_argument("--no-sandbox")
    #options.add_argument("--disable-dev-shm-usage")
    print("Initializing webdriver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print("Initialized webdriver...")
    try:
        driver.get(login_url)
        print("login url loaded...")
        time.sleep(2)

        driver.find_elements(By.CSS_SELECTOR, "input.form-control[type='email']")[0].send_keys(email)
        driver.find_elements(By.CSS_SELECTOR, "input.form-control[type='password']")[0].send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button.btn-light-primary").click()
        print("login button clicked...")
        print(f"Logged in, current URL: {driver.current_url}")
        time.sleep(5)

        actions = ActionChains(driver)
        if close_popups:
            for _ in range(4):
                actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.ENTER).perform()
            print("Closed popup.")

        driver.get(action_url)
        print("Action url loaded...")
        wait = WebDriverWait(driver, 20)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        print("Page loaded, waiting briefly...")
        time.sleep(5)

        if close_popups:
            for _ in range(5):
                actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.ENTER).perform()
            print("Closed popup.")

        timer_span = wait.until(EC.visibility_of_element_located((By.ID, "next-block-timer")))
        timer_text = timer_span.text

        if timer_text == "00:00:00":
            print("Timer is zero, maximizing window...")
            driver.maximize_window()
        else:
            claim_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[.//span[contains(text(), 'CLAIM TOKENS')]]")
            ))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", claim_button)
            time.sleep(1)  # Let page adjust
            claim_button.click()
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Button clicked successfully.")
            
        time.sleep(5)

    except WebDriverException as ex:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] WebDriver error: {ex}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_once()

