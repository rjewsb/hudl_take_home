from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.hudl.com/login"
    email= (By.ID, 'email')
    password=(By.ID, 'password')
    logInBtn=(By.ID, 'logIn' )
    failedLogin=(By.CLASS_NAME, 'login-error-container')
    sucessfulLogin=(By.CLASS_NAME, 'hui-globaluseritem')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self, email='Failure@taco.com',passwd='WontWORK!2'):
        self.browser.find_element(*self.email).send_keys(email)
        self.browser.find_element(*self.password).send_keys(passwd)
        self.browser.find_element(*self.logInBtn).click()

    def validate_failed_login(self):
        self.browser.find_element(*self.failedLogin).is_displayed()


    def validate_login_sucess(self):
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(self.sucessfulLogin)
            )
        finally:
            self.browser.find_element(*self.sucessfulLogin).is_displayed()


if __name__ == '__main__':
    main()
