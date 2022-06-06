#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[78]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

#Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[79]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[80]:


slide_elem.find('div', class_='content_title')


# In[81]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[82]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # Featured Images

# In[83]:


# Visit the URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[84]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[85]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[86]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[25]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[28]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[29]:


# Convert dataframe to html
df.to_html()


# In[31]:


browser.quit()


# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[16]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[72]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[73]:


html = browser.html
hemi_soup = soup(html, 'html.parser')


# In[74]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Loop through the images and titles
for hemisphere in range(4):
    
    # Create dictionary to hold items
    hemispheres_dict = {}

    # Find titles and click through each
    browser.find_by_css("a.product-item h3")[hemisphere].click()

    # Scrape to find the image for each hemisphere
    hemi_image = browser.find_link_by_text('Sample').first
    hemispheres_dict['img_url'] = hemi_image['href']
    
    # Scrape to find titles for each hemisphere
    hemispheres_dict['title'] = browser.find_by_css("h2.title").text
    
    # Put into dictionary and append to list
    hemisphere_image_urls.append(hemispheres_dict)
    
    # Return back for next image
    browser.back()


    
    
    
    
    
    


# In[75]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[19]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




