import requests
from selectorlib import Extractor


class Temperature:
    h = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://www.timeanddate.com/weather/'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def build_url(self):
        url = self.base_url + self.country + '/' + self.city
        return url

    def scrape(self):
        url = self.build_url()
        r = requests.get(url, headers=self.h)
        c = r.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw_data = extractor.extract(c)
        return raw_data['temp'].replace("\xa0°C", "")

    def get(self):
        scraped_content = self.scrape()
        return float(scraped_content)
