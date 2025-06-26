import pandas as pd
from src.modeling import get_pipeline, train_model
from sklearn.model_selection import train_test_split

def test_pipeline_runs():
    df = pd.DataFrame({
        'text': ["fire in forest", "no danger here", "massive flood again", "safe and quiet"],
        'target': [1, 0, 1, 0]
    })
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['target'], test_size=0.5)
    pipeline = get_pipeline()
    model = train_model(pipeline, X_train, y_train)
    preds = model.predict(X_test)
    assert len(preds) == len(y_test)
