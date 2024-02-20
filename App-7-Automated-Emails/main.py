
from news import NewsFeed
import pandas
import yagmail


df = pandas.read_excel('people.xlsx')

# url = f"{self.base_url}?qInTitle={self.interest}&from={self.from_date)&to={self.to_date}&language={self.language}&apiKey={self.api_key}"

news_feed = NewsFeed("bitcoin", "2024-02-01", "2024-02-17", "en")
print(news_feed.get())

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date="2024-02-01", to_date="2024-02-17", language="en")

    email = yagmail.SMTP(user="aditya4855@gmail.com", password="")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. {news_feed.get()}\nArdit",
               attachments="")
