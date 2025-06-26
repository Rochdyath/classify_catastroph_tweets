from src.modeling import get_pipeline, train_model, evaluate_model, plot_confusion
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/cleaned_tweet.csv")
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["target"], test_size=0.2)

pipeline = get_pipeline()
pipeline = train_model(pipeline, X_train, y_train)
y_pred = evaluate_model(pipeline, X_test, y_test)
plot_confusion(y_test, y_pred)
