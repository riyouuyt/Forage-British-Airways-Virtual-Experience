# Web Scraping for Gaining Company Insight 

## **Introduction 🚀**

Welcome to an exhilarating journey of web scraping and data analysis! 🌐💻 In this Jupyter notebook, I'll embark on a mission to collect and analyze online reviews related to British Airways, one of the world's top airlines. 🛫✈️ To accomplish this, I'll harness the power of Python and the BeautifulSoup library for web scraping.

## **Data Source: Skytrax 🌟**

Our primary data source is [Skytrax](https://www.airlinequality.com), a renowned platform for airline and airport reviews. Skytrax is a treasure trove of information, and for this task, I'll be honing in on reviews exclusively related to British Airways. Explore the [British Airways Reviews on Skytrax](https://www.airlinequality.com/airline-reviews/british-airways) for a wealth of passenger experiences.

## Libraries Used 📚

- BeautifulSoup
```python
pip install beautifulsoup4
```
- Pandas
```python
pip install pandas
```
- NumPy
```python
pip install numpy
```
- Matplotlib

```python
pip install matplotlib
```

## Web Scraping 
from the code below we try to scrape any reviews from the british airways website: 

```python
base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 10
page_size = 100

reviews = []

# for i in range(1, pages + 1):
for i in range(1, pages + 1):

    print(f"Scraping page {i}")

    # Create URL to collect links from paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Collect HTML data from this page
    response = requests.get(url)

    # Parse content
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')
    for para in parsed_content.find_all("div", {"class": "text_content"}):
        reviews.append(para.get_text())

    print(f"   ---> {len(reviews)} total reviews")
```

From the code above, We extracted 1000 reviews from Skytrax website across 10 pages.

## Data Understanding 

- DataFrame Name: Not specified, but it contains one column named "reviews."
- Number of Rows: 1000 entries.
- Column: "reviews" with a data type of object.
- Non-Null Count: 1000 non-null entries.

## Data Preprocessing

1. **Classifying Sentiments**
   
A function classify_sentiment() is created to classify reviews based on the presence of a specific phrase (in this case, 'Trip Verified'). If this phrase exists in the review, it's categorized as 'Positive'; otherwise, it's categorized as 'Negative'. This classification adds a new column called 'review_sentiment' to the DataFrame, which helps categorize reviews based on sentiment.

```python
# Function to classify reviews based on the presence of ✅ emoji
def classify_sentiment(review):
    if 'Trip Verified' in review:
        return 'Positive'
    else:
        return 'Negative'

# Create a new column "review_sentiment"
df['review_sentiment'] = df['reviews'].apply(classify_sentiment)
```

This function checks if the phrase 'Trip Verified' is present in the review text. If it is, the review is marked as 'Positive'; otherwise, it's marked as 'Negative'.

---
2. **Sentiment Analysis Summary**
   
After applying the sentiment classification function, a summary is provided that outlines the count of positive and negative reviews. This analysis helps in understanding the distribution of sentiments among the collected reviews.

**Sentiment Analysis Summary 📊**

* ✅ Positive Reviews: 791 reviews
* ❌ Negative Reviews: 209 reviews

After performing sentiment analysis on the reviews, we've uncovered interesting insights into passenger sentiments regarding British Airways:

- **Positive Reviews** ✅: There are a total of 791 positive reviews, marked with the ✅ emoji. Passengers who shared positive experiences and impressions make up the majority of the dataset.

- **Negative Reviews** ❌: There are 209 negative reviews without the ✅ emoji. These reviews indicate areas where passengers may have encountered issues or challenges during their interactions with British Airways.

This sentiment analysis provides a valuable initial perspective on passenger feedback. Further exploration and analysis can help us delve deeper into the specific aspects that contributed to these sentiments.

---
3. **Minimize All Keyword Character**

we minimize all the keyword because it doesn't mess with our analysis with different values but it's actually the same keyword, because we gonna collect an insight of the all the reviews using wordcloud. 


## Visualization Analysis

1. **Review Analysis:**

![pie chart of setiment analysis](https://github.com/riyouuyt/Forage-British-Airways-Virtual-Experience/assets/122600889/4b40d381-2d42-45f0-a32d-e3a12407498a)

Observation:

from the plot above passenger sentiments from the reviews, we observe the following distribution:

* A significant majority of the reviews, accounting for 79.1%, express satisfaction and positive experiences with the airline.

* and 20.9% of the reviews indicate areas where passengers may have encountered challenges or issues during their interactions with the airline.

This distribution underscores the predominantly positive sentiment in the reviews, while also highlighting areas of improvement for the airline's services and customer experiences.


2. **wordcloud:**

![image](https://github.com/riyouuyt/Forage-British-Airways-Virtual-Experience/assets/122600889/bb8d05fd-6653-42a4-afce-99399f43725e)

In our word cloud analysis of British Airways (BA) reviews, we embarked on a quest to uncover insightful keywords and phrases. While the word cloud did not reveal particularly prominent interesting keywords,

our focus shifted toward identifying potential negative keywords. like example heathrow, delay, still service, late etc.


