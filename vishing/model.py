//also for testing git
//still working on main branch
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))
    return model

def predict_vishing(model, features):
    prediction = model.predict(features)
    return "Vishing Attempt" if prediction == 1 else "Safe"

def load_data(csv_file, vectorizer):
    # Load dataset from a CSV file
    df = pd.read_csv(csv_file)

    # Fill NaN values with an empty string in relevant text columns using a more robust method
    df = df.assign(Attacker_Helper=df['Attacker_Helper'].fillna(""),
                   Victim=df['Victim'].fillna(""))

    # Combine the text from 'Attacker_Helper' and 'Victim' columns
    df['combined_text'] = df['Attacker_Helper'] + " " + df['Victim']
    
    # Preprocess the text data using the provided vectorizer
    X = vectorizer.fit_transform(df['combined_text'])
    
    # Assuming the 'Conversation_Type' column is the label
    y = df['Conversation_Type']
    
    return X, y