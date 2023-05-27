import csv
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Initialize stemmer, lemmatizer, and stopwords
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Function to process comments
def process_comments(comments):
    processed_comments = []
    for comment in comments:
        # Tokenize comment
        tokens = word_tokenize(comment)

        # Remove stopwords and perform stemming and lemmatization
        processed_tokens = []
        for token in tokens:
            if token.lower() not in stop_words:
                stemmed_token = stemmer.stem(token)
                lemmatized_token = lemmatizer.lemmatize(stemmed_token, pos='v')
                processed_tokens.append(lemmatized_token)

        # Add processed tokens to the list of comments
        processed_comments.append(processed_tokens)

    return processed_comments

# Read comments from CSV file
comments = []
with open('process_comments.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        comments.append(row[0])

# Process comments
processed_comments = process_comments(comments)

# Write processed words to CSV file
with open('SLT.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Processed_Words'])
    for comment in processed_comments:
        writer.writerow([comment])

