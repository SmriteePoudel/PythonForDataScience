import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class AmazonReviewScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        self.reviews = []
    
    def scrape_reviews(self, num_pages=5):
        """
        Scrape reviews from Amazon product page
        Note: Actual implementation requires handling Amazon's anti-scraping measures
        This is a placeholder method that would need customization
        """
        for page in range(1, num_pages + 1):
            try:
                response = requests.get(f"{self.url}&pageNumber={page}", headers=self.headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract review elements (placeholder - needs customization)
                review_elements = soup.find_all('div', class_='review-text')
                
                for element in review_elements:
                    review_text = element.get_text(strip=True)
                    self.reviews.append(review_text)
            
            except Exception as e:
                print(f"Error scraping page {page}: {e}")
        
        return self.reviews

class ReviewAnalyzer:
    def __init__(self, reviews):
        self.reviews = reviews
        self.df = pd.DataFrame(reviews, columns=['review'])
        self.stop_words = set(stopwords.words('english'))
        self.sia = SentimentIntensityAnalyzer()
    
    def preprocess_text(self, text):
        """Clean and preprocess text"""
        # Convert to lowercase
        text = text.lower()
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text
    
    def analyze_text_features(self):
        """Compute text-related features"""
        self.df['cleaned_review'] = self.df['review'].apply(self.preprocess_text)
        
        # Word count analysis
        self.df['word_count'] = self.df['cleaned_review'].apply(lambda x: len(x.split()))
        self.df['char_count'] = self.df['cleaned_review'].apply(len)
        self.df['avg_word_length'] = self.df['cleaned_review'].apply(lambda x: np.mean([len(word) for word in x.split()]) if x else 0)
        
        # Stopword and numeric analysis
        self.df['stopword_count'] = self.df['cleaned_review'].apply(
            lambda x: len([word for word in x.split() if word in self.stop_words])
        )
        self.df['numeric_count'] = self.df['review'].apply(
            lambda x: len(re.findall(r'\d', x))
        )
    
    def generate_wordclouds(self):
        """Generate WordClouds for all, positive, and negative reviews"""
        plt.figure(figsize=(20,15))
        
        # All reviews
        plt.subplot(2,2,1)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(self.df['cleaned_review']))
        plt.title('Word Cloud - All Reviews')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        
        # Sentiment-based WordClouds
        self.df['sentiment'] = self.df['review'].apply(
            lambda x: self.sia.polarity_scores(x)['compound']
        )
        
        # Positive reviews
        plt.subplot(2,2,2)
        positive_reviews = self.df[self.df['sentiment'] > 0]['cleaned_review']
        wordcloud_pos = WordCloud(width=800, height=400, background_color='white').generate(' '.join(positive_reviews))
        plt.title('Word Cloud - Positive Reviews')
        plt.imshow(wordcloud_pos, interpolation='bilinear')
        plt.axis('off')
        
        # Negative reviews
        plt.subplot(2,2,3)
        negative_reviews = self.df[self.df['sentiment'] < 0]['cleaned_review']
        wordcloud_neg = WordCloud(width=800, height=400, background_color='white').generate(' '.join(negative_reviews))
        plt.title('Word Cloud - Negative Reviews')
        plt.imshow(wordcloud_neg, interpolation='bilinear')
        plt.axis('off')
        
        plt.tight_layout()
        plt.savefig('review_wordclouds.png')
        plt.close()
    
    def plot_text_distributions(self):
        """Plot distributions of various text features"""
        plt.figure(figsize=(20,15))
        
        # Word Count Distribution
        plt.subplot(2,3,1)
        sns.histplot(self.df['word_count'], kde=True)
        plt.title('Word Count Distribution')
        
        # Character Count Distribution
        plt.subplot(2,3,2)
        sns.histplot(self.df['char_count'], kde=True)
        plt.title('Character Count Distribution')
        
        # Stopword Count Distribution
        plt.subplot(2,3,3)
        sns.histplot(self.df['stopword_count'], kde=True)
        plt.title('Stopword Count Distribution')
        
        # Numeric Count Distribution
        plt.subplot(2,3,4)
        sns.histplot(self.df['numeric_count'], kde=True)
        plt.title('Numeric Count Distribution')
        
        # Average Word Length Distribution
        plt.subplot(2,3,5)
        sns.histplot(self.df['avg_word_length'], kde=True)
        plt.title('Average Word Length Distribution')
        
        plt.tight_layout()
        plt.savefig('text_feature_distributions.png')
        plt.close()
    
    def sentiment_scatter_plot(self):
        """Create Scatter Intensity Plot of Sentiments"""
        plt.figure(figsize=(12,8))
        
        # Scatter plot with color intensity based on sentiment
        scatter = plt.scatter(
            self.df.index, 
            self.df['sentiment'], 
            c=self.df['sentiment'], 
            cmap='RdYlGn', 
            alpha=0.7
        )
        
        plt.colorbar(scatter)
        plt.title('Sentiment Intensity Scatter Plot')
        plt.xlabel('Review Index')
        plt.ylabel('Sentiment Score')
        plt.tight_layout()
        plt.savefig('sentiment_scatter.png')
        plt.close()
    
    def save_analysis(self, filename='amazon_review_analysis.csv'):
        """Save analyzed data to CSV"""
        self.df.to_csv(filename, index=False)
    
    def run_full_analysis(self):
        """Run complete analysis pipeline"""
        self.analyze_text_features()
        self.generate_wordclouds()
        self.plot_text_distributions()
        self.sentiment_scatter_plot()
        self.save_analysis()



print("Amazon Review Analysis Script is ready!")
