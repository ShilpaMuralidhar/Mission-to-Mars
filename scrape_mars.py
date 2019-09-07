# import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# Create an empty dictionary to import into Mongo
mars_info = {}

# NASA Mars News
def scrape_mars_news():
    try:
        # initialize the browzer
        browser = init_browser()

        # browser.is_element_present_by_css("div.content_title", wait_time=1)

        # Visit NASA news url through splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        # HTML object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve the latest element that contains news title and news_paragraph
        title = soup.find(class_='content_title').find('a').text
        nasa_p = soup.find(class_='article_teaser_body').text

        # Dictionary entry from Mars News
        mars_info['news_title'] = title
        mars_info['nasa_paragraph'] = nasa_p

        return mars_info

    finally:
        browser.quit()

# Featured Images    
def scrape_mars_images():
    try:
         # initialize the browzer
        browser = init_browser()

        # browser.is_element_present_by_css("image.jpg", wait_time=1)

        # Visit NASA news url through splinter module
        image_featured_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_featured_url)

        # HTML object
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')

        # Retrieve the image url
        featured_image_url= soup.find('article')['style'].replace('background-image: url(', '').replace(');','')[1:-1]

        # Main Url 
        main_url = 'https://www.jpl.nasa.gov'

        # Merge main url and the image url
        featured_image_url = main_url + featured_image_url

         # Dictionary entry from Mars images
        mars_info['image_featured_url'] = image_featured_url
       
        return mars_info
        
    finally:
        browser.quit()
        
# Mars Weather    
def scrape_mars_weather():
    try:
          # initialize the browzer
        browser = init_browser()

        # browser.is_element_present_by_css("div", wait_time=1)

        # Visit NASA news url through splinter module
        mars_weather = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(mars_weather)

        # HTML object
        html_weather = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_weather, 'html.parser')

        # Retrieve the tweet
        mars_tweets  = soup.find_all('div', class_= 'js-tweet-text-container')

        for tweet in mars_tweets:
            mars_weather = tweet.find('p').text
            if 'solar' and 'silent' in mars_weather:
                print(mars_weather)
                break
            else:
                pass

        mars_tweets  = soup.find_all('div', class_= 'js-tweet-text-container')

        for tweet in mars_tweets:
            mars_weather = tweet.find('p').text
            if 'Insight' and 'gusting' in mars_weather:
                print(mars_weather)
                break
            else:
                pass



        # Dictionary entry from Mars images
        mars_info['mars_weather'] = mars_weather
       
        return mars_info
        
    finally:
        browser.quit()


# Mars Facts   
def scrape_mars_facts():
    try:
          # initialize the browzer
        browser = init_browser()

        # browser.is_element_present_by_css("div", wait_time=1)

        # Visit NASA news url through splinter module
        url = 'https://space-facts.com/mars/'
        browser.visit(url)

        mars_table = pd.read_html(url)
        df_mars = mars_table[0]
        df_mars.columns = ['Mars-Earth-Comparison', 'Mars', 'Earth']
        df_mars.drop(['Earth'], axis=1)

        # Dictionary entry from Mars images
        mars_info['mars_table'] = mars_table
       
        return mars_info
        
    finally:
        browser.quit()


# Mars Weather    
def scrape_mars_hemisphere():
    try:
          # initialize the browzer
        browser = init_browser()

        # browser.is_element_present_by_css("div", wait_time=1)

        # Visit NASA news url through splinter module
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        # HTML object
        hemisphere_html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(hemisphere_html, 'html.parser')

        # Retrieve the tweet
        items = soup.find_all('div', class_= 'item')

        # Empty list
        hemisphere_url = []

        # Store main url
        hemisphere_main_url = 'https://astrogeology.usgs.gov'

        #loop the items
        for item in items:
            title = item.find('h3').text
            individual_url= item.find('a', class_= 'itemLink product-item')['href']
            full_url = hemisphere_main_url+individual_url
            browser.visit(full_url)
            full_url_html = browser.html
            soup = BeautifulSoup(full_url_html, 'html.parser')

            image_url = soup.find('img', class_= 'wide-image')['src']
            hemisphere_url.append({'title': title, 'image_url': image_url})
            
        hemisphere_url



        # Dictionary entry from Mars images
        mars_info['hemisphere_url'] = hemisphere_url
       
        return mars_info
        
    finally:
        browser.quit()
