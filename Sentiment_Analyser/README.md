# Policy News Sentiment Analysis Tool README

## Overview
This script fetches and analyzes news articles related to economic policies (like monetary and fiscal policies) from NewsAPI. It uses natural language processing (NLP) to perform sentiment analysis on the headlines and visualizes the sentiment distribution across various policy keywords. The script leverages libraries such as `requests`, `pandas`, `nltk`, `matplotlib`, and `seaborn`.

## Requirements
To run this script, you need the following Python libraries installed:
- `requests`
- `pandas`
- `nltk`
- `matplotlib`
- `seaborn`

Install them using pip:
```bash
pip install requests pandas nltk matplotlib seaborn
```

Additionally, you need an API key from [NewsAPI](https://newsapi.org/). Replace `'YOUR_API_KEY'` in the script with your actual API key.

## Usage
1. **Set the Country Code**:
   - Change the `country_code` variable to the relevant country code (e.g., `'us'` for the United States).

2. **Run the Script**:
   - The script fetches articles related to the policy keywords defined in the `policy_keywords` list (e.g., `'monetary policy'`, `'interest rates'`).

3. **Output**:
   - The script performs sentiment analysis using NLTK's VADER SentimentIntensityAnalyzer and visualizes the sentiment distribution for each policy keyword.

## Features

### 1. Fetch News Articles
The script fetches news sources and articles from the specified country using NewsAPI:
```python
url_sources = 'https://newsapi.org/v2/top-headlines/sources?country={}&apiKey={}'.format(country_code, api_key)
```

### 2. Keyword Matching
Filters articles based on the presence of the specified policy keywords in their titles and descriptions.

### 3. Sentiment Analysis
Applies NLP to classify the sentiment (Positive, Negative, Neutral) of each article headline:
- Uses NLTK's VADER SentimentIntensityAnalyzer.
- Classifies sentiment based on the compound score:
  - **Positive**: `compound >= 0.05`
  - **Negative**: `compound <= -0.05`
  - **Neutral**: otherwise

### 4. Data Visualization
Creates a bar plot to visualize the distribution of sentiment for each policy keyword:
- Displays the number of articles with Positive, Negative, and Neutral sentiment per keyword.

### 5. Export to CSV
Saves the processed DataFrame with sentiment scores to a CSV file named `'policy_news_sentiment_<country_code>.csv'`.

## Setup Instructions
1. Obtain an API key from [NewsAPI](https://newsapi.org/).
2. Replace `'YOUR_API_KEY'` in the script with your actual API key.
3. Ensure you have internet access to make API requests and download news data.

## Customization
- **Keywords**: Modify the `policy_keywords` list to target different keywords.
- **Country**: Change the `country_code` variable to fetch news from different countries.
- **Date Range and Filters**: Adjust API parameters in the `url` if needed, such as language or sorting options.

## Example Outputs

### 1. Article Data Preview
Displays the first few rows of the DataFrame with articles and their matching keywords.

### 2. Sentiment Bar Plot
A bar plot showing the distribution of Positive, Negative, and Neutral sentiment for each policy keyword.

## Important Notes
- Make sure to handle rate limits when using the NewsAPI. The script includes a time delay (`time.sleep(1)`) between API requests to avoid hitting limits.
- NLTK's VADER lexicon will be downloaded automatically if not already present.

## License
This script is open-source. Feel free to modify it to suit your analysis needs.

Enjoy analyzing news sentiment trends! 📰📊