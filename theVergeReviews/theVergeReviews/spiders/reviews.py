# Importing necessary libraries
from urllib.parse import urljoin

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from theVergeReviews.items import ThevergereviewsItem


# Defining a new spider class ReviewSpider
class ReviewSpider(CrawlSpider):
    name = 'the_verge_reviews'  # Setting the name of the spider
    # Setting the domain(s) that the spider is allowed to crawl
    allowed_domains = ['theverge.com']
    # Setting the URL(s) to start crawling from
    start_urls = ['https://www.theverge.com/reviews']
    # Defining a regular expression pattern to match review URLs
    pattern = r'https://www.theverge.com/\d+/[^\s]+$'
    # Defining the domain of the website being scraped
    domain = 'https://www.theverge.com'

    # Defining the crawling rule to follow and the callback function to parse the response
    rules = (
        Rule(LinkExtractor(allow=(pattern, )), callback='parse_item',
             follow=True, cb_kwargs={"is_review": True}, ),

    )

    # Parsing the extracted response and storing it in the item object
    def parse_item(self, response, is_review):

        # Checking if the response contains a review
        if is_review:
            # Creating a new item object to store the scraped data
            item = ThevergereviewsItem()
            # Storing the URL of the review in the item
            item['url'] = response.url
            # Storing the title of the review in the item
            item['title'] = response.xpath(
                '//h1/text()| //h2/text() | //*[@class ="hover:shadow-underline-blurple dark:hover:shadow-underline-franklin"]/text()').get()
            # Storing the name of the author of the review in the item
            item['author'] = response.xpath(
                "//a[contains(@href,'/authors/')]/text()").get()
            # Storing the link to the author's page in the item
            item['author_link'] = urljoin(self.domain, response.xpath(
                "//a[contains(@href,'/authors/')]/@href").get())

            # Returning the item to the scrapy engine for further processing
            yield item
        else:
            pass  # If the response is not a review, do nothing.
