from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

app = Flask(__name__)

# Load and train the model (using the same logic from your notebook)
def load_and_train_model():
    # Load the training data
    train_data = pd.read_csv('./titanic/train.csv')
    
    # Data preprocessing (same as your notebook)
    train_data = train_data.dropna(subset=['Age'])
    train_data = train_data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
    train_data['Embarked'] = train_data['Embarked'].fillna(train_data['Embarked'].mode()[0])
    
    # One-hot encoding
    train_data = pd.get_dummies(train_data, columns=['Sex', 'Embarked'], drop_first=True)
    train_data['Age'] = train_data['Age'].astype(int)
    
    # Prepare features and target
    X = train_data.drop(columns=['Survived'], axis=1)
    y = train_data['Survived']
    
    # Train the model with the best parameters from your grid search
    model = DecisionTreeClassifier(
        criterion='gini', 
        max_depth=5, 
        min_samples_split=3, 
        random_state=42
    )
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    
    return model, X.columns.tolist()

# Load the model
model, feature_columns = load_and_train_model()

def preprocess_user_input(user_data):
    """Preprocess user input to match the training data format"""
    # Create a DataFrame with the user input
    df = pd.DataFrame([user_data])
    
    # One-hot encode Sex and Embarked
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
    
    # Ensure all required columns are present
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0
    
    # Reorder columns to match training data
    df = df[feature_columns]
    
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        user_data = {
            'Pclass': int(request.form['pclass']),
            'Age': int(request.form['age']),
            'SibSp': int(request.form['sibsp']),
            'Parch': int(request.form['parch']),
            'Fare': float(request.form['fare']),
            'Sex': request.form['sex'],
            'Embarked': request.form['embarked']
        }
        
        # Preprocess the input
        processed_data = preprocess_user_input(user_data)
        
        # Make prediction
        prediction = model.predict(processed_data)[0]
        probability = model.predict_proba(processed_data)[0]
        
        # Calculate survival probability
        survival_prob = probability[1] * 100  # Probability of survival
        death_prob = probability[0] * 100     # Probability of death
        
        result = {
            'survived': bool(prediction),
            'survival_probability': round(survival_prob, 1),
            'death_probability': round(death_prob, 1),
            'user_data': user_data
        }
        
        return render_template('result.html', result=result)
    
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)