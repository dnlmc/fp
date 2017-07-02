ua = UserAgent()

# initialize chrome webdriver & navigate to URL
driver = webdriver.Chrome('~/chromedriver')
driver.get('https://m.faceplace.com/daniels_friend/year/2017/')

sleep(5)

# enter login credentials
login = driver.find_element_by_name('email')
login.send_keys('my_actual_email@gmail.com')

sleep(5)

# enter password
pword = driver.find_element_by_id('u_0_2')
pword.send_keys('my_actual_password')

sleep(5)

# submit login
button = driver.find_element_by_id('u_0_6')
button.click()

sleep(5)

# scroll to bottom of the page a bunch of times to load all posts
for i in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

# scrape page source code
friendsoup17 = BeautifulSoup(driver.page_source,'html.parser')