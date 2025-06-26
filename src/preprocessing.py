import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    tagged = pos_tag(tokens)
    return [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in tagged]

def cleen_tweet(tweet):
    # Minuscule
    tweet = tweet.lower()
    
    # Suppression des URLs, mentions, hashtags
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet)
    tweet = re.sub(r"@\w+", '', tweet)
    tweet = re.sub(r"#", '', tweet)
    
    # Suppression ponctuation et chiffres
    tweet = re.sub(r"[^a-z\s]", '', tweet)
    
    # Tokenisation
    tokens = nltk.word_tokenize(tweet)
    
    # Filtrage : mots courts + stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words and len(t) >= 3]
    
    # Lemmatisation
    tokens = lemmatize_tokens(tokens)
    
    return tokens