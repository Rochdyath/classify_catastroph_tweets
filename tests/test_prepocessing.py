from src.preprocessing import cleen_tweet

def test_empty_text():
    assert cleen_tweet("") == []

def test_punctuation_and_digits():
    assert cleen_tweet("123 !!! ...") == []

def test_stopwords_removal():
    text = "This is an example with some stopwords"
    result = cleen_tweet(text)
    assert "this" not in result
    assert "is" not in result

def test_min_token_length():
    result = cleen_tweet("ok hi a big deal win")
    assert all(len(t) > 2 for t in result)

def test_lemmatizer_effect():
    tokens = cleen_tweet("running runs ran")
    assert len(set(tokens)) == 1
