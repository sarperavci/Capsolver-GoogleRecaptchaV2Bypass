from selenium import webdriver
import time
import capsolver

class CapsolverRecaptchaV2Bypasser:
    def __init__(self, webdriver:webdriver.Chrome , page_url, page_key, api_key):
        capsolver.api_key = api_key
        self.page_url = page_url
        self.page_key = page_key
        self.solution = None
        self.webdriver = webdriver

    def solve_recaptcha(self):
        self.solution = capsolver.solve({
            "type": "ReCaptchaV2TaskProxyless",
            "websiteURL": self.page_url,
            "websiteKey": self.page_key,
        })

        self.webdriver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": self.solution["userAgent"]
        })
        time.sleep(.1)
        
        self.webdriver.execute_script(f"document.getElementById('g-recaptcha-response').value = '{self.solution['gRecaptchaResponse']}';")
        time.sleep(.1)
