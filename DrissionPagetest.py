from DrissionPage import ChromiumPage
import time
import capsolver

# Consider using environment variables for sensitive information
capsolver.api_key = "CAP-2BA1B8ACE40295789C28A59A5402DD8A"
PAGE_URL = "https://google.com/recaptcha/api2/demo"
PAGE_KEY = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"

def solve_recaptcha_v2(url,key):
    solution = capsolver.solve({
        "type": "ReCaptchaV2TaskProxyless",
        "websiteURL": url,
        "websiteKey":key,
    })
    return solution

#print("Solving reCaptcha v2")
#solution = solve_recaptcha_v2(PAGE_URL, PAGE_KEY)
## solution format: {"gRecaptchaResponse": "03AGdBq...","userAgent":"Mozilla/5.0 ..."}
# 
page  = ChromiumPage()
#page.set.user_agent(solution["userAgent"])
page.get("https://google.com/recaptcha/api2/demo")
#page.run_js(f"document.getElementById('g-recaptcha-response').value = '{solution['gRecaptchaResponse']}';")
#time.sleep(5)
#page.click("Submit")
#
#time.sleep(55)
#page.close()