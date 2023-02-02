import scrapy

class takhfifanspider(scrapy.Spider):
    name = "Takhfifan"
    start_urls = ["https://takhfifan.com/tehran/recreational-sports"]
    
    def parse(self,response):
        for card in response.css('div.tile-vendor-card-list__item'):
            tickets = card.css("div.vendor-card-box__solid-count-list__item")
            if tickets != None:
                tickets = tickets.split(' ')[0]
            yield{
                'title' : card.css('div.vendor-card-box__title-part p.vendor-card-box__title-text::text').get(),
                'location' : card.css('div.vendor-card-box__location.has-border span::text').get(),
                'rate' : card.css('p.rate-badge__rate-value::text').get(),
                'number_of_voters' : card.css('p.rate-badge__rate-count::text').get(),
                'number of sold tickets' : (card.css('div.vendor-card-box__sold-count p::text').get()).split(' ')[0],
                'discount(%)' : card.css('div.vendor-card-box__percent span::text').getall()[2] + card.css('div.vendor-card-box__percent span::text').getall()[3],
                'more_detail' : f"https://takhfifan.com{card.css('div.vendor-card-box a::attr(href)').get()}"
            }
            