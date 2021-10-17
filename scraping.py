import pandas as pd
# import splinter and beautiful soup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# set up splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# set url and visit the mars news site
url ='https://redplanetscience.com'
browser.visit(url)
## optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

#set up html parser
html= browser.html
news_soup = soup(html,'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# add get_text() to return only the text of that element
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# use parent element to find paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## JPL Space Images Featured Image

# visit url
url = 'https://spaceimages-mars.com'
browser.visit(url)

# find and click 'full image' button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# parse image with bsoup
html = browser.html
img_soup = soup(html, 'html.parser')

# find relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

# use base url to create absolute url
img_url = f'spaceimages-mars.com/{img_url_rel}'
img_url

# ## mars facts
# read html table into dataframe
df = pd.read_html('https://galaxyfacts-mars.com')[0]

df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# push dataframe into html format
df.to_html()

# end session
browser.quit()


