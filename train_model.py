import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("phishing.csv")

selected_features = [
    'qty_dot_url',
    'qty_hyphen_url',
    'qty_underline_url',
    'qty_slash_url',
    'qty_questionmark_url',
    'qty_equal_url',
    'qty_at_url',
    'qty_and_url',
    'qty_exclamation_url',
    'qty_space_url',
    'qty_tilde_url',
    'qty_comma_url',
    'qty_plus_url',
    'qty_asterisk_url',
    'qty_hashtag_url',
    'qty_dollar_url'
]

X = df[selected_features]
y = df['phishing']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved!")
