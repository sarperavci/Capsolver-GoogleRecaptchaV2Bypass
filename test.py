from CapsolverRecaptchaV2Bypasser import CapsolverRecaptchaV2Bypasser
from selenium import webdriver
import time

CAPSOLVER_API_KEY = "YOUR_API_KEY"
page_url = "https://google.com/recaptcha/api2/demo"
page_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-" # This can be found in the data-sitekey attribute of the reCaptcha element

page = webdriver.Chrome()
page.get( page_url )
recaptchaBypasser = CapsolverRecaptchaV2Bypasser(page, page_url, page_key, CAPSOLVER_API_KEY)

print("Solving reCaptcha v2...")
t0 = time.time()
recaptchaBypasser.solve_recaptcha()
print( f"Time elapsed: {time.time() - t0:.2f} seconds" )

# Verify the solution by submitting the form
page.find_element(value="recaptcha-demo-submit").click()

input("Press Enter to close the browser")

page.quit()

 