import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import TimeoutException

#to store the CSV file
OUTPUT_PATH = '/Users/sushmapawar/Desktop/Projects/SentimentalAnalysis/'

city = input('Enter your City:')
print('City Entered:\t\t',city)
hotelCount = int(input('Enter number of hotels:'))
print('Number of Restaurants user wants:\t\t',hotelCount)
maxReviewCount = int(input('Enter number of reviews:'))
print('Number of reviews user wants to Scrape:\t\t',maxReviewCount)

url = "https://www.zomato.com/" + city +'/dine-out'
print("\nwebsite visited is:\t",url)

#no need to update the chrome it will install and then run
s = Service(ChromeDriverManager().install())
chromeOptions = Options()
driver = webdriver.Chrome(options=chromeOptions)
print("\n\nLaunching CHROME browser.........")

# chromeOptions = Options()
# driver = webdriver.Chrome(options=chromeOptions)
driver.get(url)
driver.maximize_window()

# Scroll down to bottom and take the integer value of it
total_height = int(driver.execute_script("return document.body.scrollHeight"))

#scroll till the restaurant names get visible
driver.execute_script("window.scrollTo(0, 800)")
time.sleep(5)

# list to get the data for restaurants
lst = []
# list to get restaurant URLS
urls = []

# for loop to scroll and get the URLs of restaurants
for k in range(1, total_height):
    # if length of URLS is greater than the user entered hotelCount then break
    if len(urls) > hotelCount:
        break
    # slow scroll down in k times
    driver.execute_script("window.scrollTo(0, {});".format(k*70))
    element = driver.find_element(By.XPATH,'(//div[@class="jumbo-tracker"])['+str(k)+']//a[1]')
    # list of url links
    urls.append(element.get_attribute('href'))

# to get the data for the restaurants entered by user
for i in range (1,hotelCount+1):
    driver.get(urls[i])
    driver.implicitly_wait(3)
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '(//div//h1)[2]')))
    # to get the Restaurant names
    title = driver.find_element(By.XPATH, '(//div//h1)[2]').text
    # to get the Restaurant ratings
    res_reviews = driver.find_element(By.CLASS_NAME, 'cILgox').text
    # to get the link of reviews by user
    driver.find_element(By.LINK_TEXT,'Reviews').click()
    reviewCount = 1
    while reviewCount < maxReviewCount:
        driver.implicitly_wait(10)
        # to handle state element exception
        WebDriverWait(driver, 40).until(expected_conditions.presence_of_element_located((By.XPATH, '((//a[contains(@rel,"noreferrer noopener")]/ancestor::section)[3]/following-sibling::p)[1]')))
        for j in range(1,6):
            if reviewCount <= maxReviewCount:
                try:
                    # Locator to access the username
                    userName = driver.find_element(By.XPATH,'(//a[contains(@href,"https://www.zomato.com/")]//p)['+str(j)+']').text
                    # Locator to access the written reviews
                    review = driver.find_element(By.XPATH,'((//a[contains(@rel,"noreferrer noopener")]/ancestor::section)[3]/following-sibling::p)['+str(j)+']').text
                    # to get the rating given by each user
                    review_rating = driver.find_element(By.XPATH,
                                                  '(//body//div[@id="root"]//div//div//div//div//div//div[*]//div[1]//div[1]//div[1]//div[1]//div[1])['+str(j)+']').text
                    # to create the dictionary
                    restaurant = {'Restaurant_Name': title,
                                  'Restaurant_Rated': res_reviews,
                                   'Review_Written_By': userName,
                                  'User_Rated_Restaurant': review_rating,
                                  'Written_Review': review
                                  }
                    lst.append(restaurant)
                    reviewCount += 1
                except:
                    break
            else:
                break
        # to click on next button to get next page reviews
        try:
            driver.find_element(By.XPATH,'(//*[local-name()="title" and text()="chevron-right"])//parent::*[local-name()="svg"]').click()
        except:
            # if next button is not clicked break
            break
    # to print the restaurant number and restaurant name
    print(i,":",title)

# to create the dataframe
df = pd.DataFrame(lst)
print(df)

# download the csv
df.to_csv(OUTPUT_PATH  + 'sentiment_analysis_output.csv')