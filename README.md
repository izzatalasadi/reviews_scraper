# reviews_scraper
The script defines a spider that can crawl theverge.com and extract review information from the pages that match a specific regular expression pattern.


## run the code:
* cd theVergeReviews/theVergeReviews
* scrapy runspider  reviews.py  -o reviews.csv  -t  csv

## after you run the code you will get a csv file with reviews includes:
author,author_link,title,url


## important steps to create similar project
  Create a new project called theVergeReviews:
  scrapy startproject theVergeReviews

  Add some customized settings to settings.py
  ### Page visit limit
  CLOSESPIDER_PAGECOUNT = 20


  ### User agent to mimic browser requests
  USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'



 ### Adding items (Field objects) to items.py
class ThevergereviewsItem(scrapy.Item):
   url = scrapy.Field()
   title = scrapy.Field()
   author = scrapy.Field()
   author_link = scrapy.Field()

     Pass
 ## Create a new python file (reviews.py), 
  theVergeReviews → theVergeReviews → spiders → reviews.py 
  Import important libraries and the items, and create a class ReviewSpider(CrawlSpider)
  
  ## Comments added for each line of code in reviews.py
