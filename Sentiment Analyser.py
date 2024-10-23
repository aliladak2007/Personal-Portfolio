import requests
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import time
import urllib.parse

# Replace 'YOUR_API_KEY' with your actual API key from NewsAPI
api_key = '3d335c419ede4797b1a7fc72013fdbd6'

# Define the country code (e.g., 'gb' for the United Kingdom)
country_code = 'gb'  # Change this to the country code you're interested in

# Define a list of policy keywords
policy_keywords = ['monetary policy', 'interest rates', 'quantitative easing', 'fiscal policy']

# Get sources from the specified country
url_sources = (
    'https://newsapi.org/v2/top-headlines/sources?'
    'country={}&'
    'apiKey={}'
).format(country_code, api_key)

response_sources = requests.get(url_sources)
data_sources = response_sources.json()  # Corrected line

if data_sources['status'] == 'ok':
    sources = data_sources['sources']
    source_ids = [source['id'] for source in sources]
    sources_str = ','.join(source_ids)
else:
    print('Error fetching sources.')
    print('Error code:', data_sources.get('code', 'No code provided'))
    print('Message:', data_sources.get('message', 'No message provided'))
    sources_str = ''

# Initialize an empty list to hold all articles
all_articles = []

# Loop over each keyword and fetch articles
for keyword in policy_keywords:
    # URL-encode the keyword
    encoded_keyword = urllib.parse.quote(keyword)
    
    # Construct the API request URL
    url = (
        'https://newsapi.org/v2/everything?'
        'q={}&'
        'sources={}&'
        'language=en&'
        'sortBy=publishedAt&'
        'pageSize=100&'
        'apiKey={}'
    ).format(encoded_keyword, sources_str, api_key)
    
    # Make the API request
    response = requests.get(url)
    data = response.json()
    
    # Check if the request was successful
    if data['status'] == 'ok':
        articles = data.get('articles', [])
        all_articles.extend(articles)
        print(f"Fetched {len(articles)} articles for keyword: '{keyword}'")
    else:
        print(f"Error fetching data for keyword: '{keyword}'")
        print('Error code:', data.get('code', 'No code provided'))
        print('Message:', data.get('message', 'No message provided'))
        continue  # Skip to the next keyword if there's an error
    
    time.sleep(1)  # Optional: wait to avoid rate limits

# Check if any articles were fetched
print(f"Total articles fetched: {len(all_articles)}")
if not all_articles:
    print("No articles were fetched. Exiting the program.")
    exit()

# Convert the list of articles to a DataFrame
df_articles = pd.DataFrame(all_articles)

# Fill missing 'title' and 'description' with empty strings
df_articles['title'] = df_articles['title'].fillna('')
df_articles['description'] = df_articles['description'].fillna('')

# Drop duplicates based on the 'url' field
df_articles.drop_duplicates(subset='url', inplace=True)

# Define a function to check which keywords are in the article's title or description
def get_matching_keywords(row):
    content = row['title'] + ' ' + row['description']
    matching_keywords = [keyword for keyword in policy_keywords if keyword.lower() in content.lower()]
    return matching_keywords

# Apply the function to each article
df_articles['matching_keywords'] = df_articles.apply(get_matching_keywords, axis=1)

# Filter out articles with no matching keywords
df_articles = df_articles[df_articles['matching_keywords'].map(len) > 0]

# Check if any articles remain after filtering
if df_articles.empty:
    print("No articles match the specified policy keywords. Exiting the program.")
    exit()

# Print first few rows to inspect data
print("First few rows of the DataFrame after filtering:")
print(df_articles[['title', 'matching_keywords']].head())

# Download the VADER lexicon if not already downloaded
nltk.download('vader_lexicon', quiet=True)

# Initialize the sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Define a function to get sentiment scores
def get_sentiment(text):
    if isinstance(text, str) and text.strip():
        return sia.polarity_scores(text)
    else:
        return {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}

# Apply the function to the headlines
df_articles['sentiment_scores'] = df_articles['title'].apply(get_sentiment)

# Expand the sentiment scores into separate columns
df_sentiment = df_articles['sentiment_scores'].apply(pd.Series)
df_articles = pd.concat([df_articles, df_sentiment], axis=1)

# Define a function to classify sentiment based on the compound score
def classify_sentiment(compound_score):
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply the classification function to the compound scores
df_articles['Sentiment'] = df_articles['compound'].apply(classify_sentiment)

# Explode the matching_keywords list to have one keyword per row
df_exploded = df_articles.explode('matching_keywords')

# Check if df_exploded is not empty
if df_exploded.empty:
    print("No data to visualize after exploding matching_keywords. Exiting the program.")
    exit()

# Print data after exploding matching_keywords
print("Data after exploding matching_keywords:")
print(df_exploded[['title', 'matching_keywords', 'Sentiment']].head())

# Group by policy keyword and sentiment
sentiment_by_policy = df_exploded.groupby(['matching_keywords', 'Sentiment']).size().reset_index(name='Counts')

# Pivot the data to have sentiments as columns
sentiment_pivot = sentiment_by_policy.pivot(index='matching_keywords', columns='Sentiment', values='Counts').fillna(0)

# Calculate the total counts for sorting
sentiment_pivot['Total'] = sentiment_pivot.sum(axis=1)

# Sort the DataFrame by total counts
sentiment_pivot = sentiment_pivot.sort_values('Total', ascending=False)

# Remove the 'Total' column after sorting
sentiment_pivot = sentiment_pivot.drop(columns=['Total'])

# Reset index for plotting
sentiment_pivot = sentiment_pivot.reset_index()

# Melt the DataFrame for seaborn
sentiment_melted = sentiment_pivot.melt(id_vars='matching_keywords', var_name='Sentiment', value_name='Counts')

# Ensure 'Counts' is integer type
sentiment_melted['Counts'] = sentiment_melted['Counts'].astype(int)

# Set Seaborn style
sns.set_style('whitegrid')

# Create a color palette
palette = {'Positive': 'green', 'Negative': 'red', 'Neutral': 'gray'}

# Plot sentiment distribution for each policy keyword
plt.figure(figsize=(12, 8))
ax = sns.barplot(
    data=sentiment_melted,
    x='Counts',
    y='matching_keywords',
    hue='Sentiment',
    palette=palette,
    ci=None
)

# Add data labels to each bar
for p in ax.patches:
    width = p.get_width()
    plt.text(
        width + 0.1,  # Offset to the right of the bar
        p.get_y() + p.get_height() / 2 + 0.1,  # Vertically centered with slight adjustment
        '{:.0f}'.format(width),  # Value label
        ha='left',  # Horizontal alignment
        va='center'  # Vertical alignment
    )

# Set titles and labels
plt.title('Sentiment Analysis by Policy Keyword in {}'.format(country_code.upper()), fontsize=16)
plt.xlabel('Number of Articles', fontsize=14)
plt.ylabel('Policy Keyword', fontsize=14)

# Adjust legend
plt.legend(title='Sentiment', fontsize=12, title_fontsize=12, loc='best')

plt.tight_layout()
plt.show()

# Save the DataFrame to a CSV file
df_articles.to_csv('policy_news_sentiment_{}.csv'.format(country_code), index=False)
