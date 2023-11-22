import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.stem import PorterStemmer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 10
page_size = 100
reviews = []

for i in range(1, pages + 1):
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"
    response = requests.get(url)
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')
    for para in parsed_content.find_all("div", {"class": "text_content"}):
        reviews.append(para.get_text())

df = pd.DataFrame()
df["reviews"] = reviews

def classify_sentiment(review):
    if 'Trip Verified' in review:
        return 'Positive'
    else:
        return 'Negative'

df['review_sentiment'] = df['reviews'].apply(classify_sentiment)

stemmer = PorterStemmer()
def stem_text(text):
    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)

df['reviews'] = df['reviews'].apply(stem_text)

word_freq = df['reviews'].str.split(expand=True).stack().value_counts()
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

print("Word Review Analysis:")
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

data = {
    'review_sentiment': ['Positive', 'Negative'],
    'counts': [df['review_sentiment'].value_counts()['Positive'], df['review_sentiment'].value_counts()['Negative']]
}
df = pd.DataFrame(data)
total_reviews = df['counts'].sum()
df['percentages'] = (df['counts'] / total_reviews) * 100

colors = ['darkgreen', 'palegreen']
plt.figure(figsize=(15, 8))
plt.pie(df['percentages'], labels=df['review_sentiment'], autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Sentiment Analysis', fontsize=18, fontweight='bold')
plt.show()
