from selenium import webdriver
from selenium.webdriver.common.by import By
from models import NewsModel
# Create a WebDriver instance (for Chrome in this example)
driver = webdriver.Chrome()

# Navigate to the website with news articles
driver.get("https://www.goal.com/en-us/news")

# # Find and extract news titles and paragraphs
# news_articles = driver.find_elements(by=By.CSS_SELECTOR , value=".poster-wrapper")  # Adjust the selector as needed
# print(news_articles)

news_articles = driver.find_elements(by=By.CSS_SELECTOR, value='[data-testid="card-title-url"]')
print(news_articles)


news_link =  []
for item in news_articles:
    raw_link = item.get_attribute('href')
    news_link.append(raw_link)
    
for item in news_link:
    try:
        driver.get(item)
        title  =  driver.find_element(by=By.CSS_SELECTOR, value='[data-testid="article-title"]').text
        descriptionList =  driver.find_element(by=By.CSS_SELECTOR, value='[data-testid="article-body"]').find_elements(by=By.TAG_NAME, value='p' )
        description = ''
        for item in descriptionList:
            description += item.text
            description+='\n'

        print(description)
        news  = NewsModel(title=title,  description=description)
        news.create()
        
        
    except :
        continue


driver.quit()
