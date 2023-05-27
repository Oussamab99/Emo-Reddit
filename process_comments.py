import re,csv,emoji

# Function to remove special characters
def remove_special_characters(text):
    # Remove special characters using regular expressions
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Function to remove URLs
def remove_urls(text):
    # Remove URLs using regular expressions
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    return text

# Function to remove emojis
def remove_emojis(text):
    # Remove emojis using the emoji library
    text = emoji.demojize(text)
    text = re.sub(r':[a-zA-Z_]+:', '', text)
    return text


# Read the contents of the comments.csv file
with open('comments.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    comments = [row[0] for row in reader]


# Process the comments to remove special characters, URLs, and emojis
processed_comments = []
for comment in comments:
    processed_comment = remove_special_characters(comment)
    processed_comment = remove_urls(processed_comment)
    processed_comment = remove_emojis(processed_comment)
    processed_comments.append(processed_comment)


# Write the processed comments back to the comments.csv file
with open('process_comments.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for comment in processed_comments:
        writer.writerow([comment])

    
