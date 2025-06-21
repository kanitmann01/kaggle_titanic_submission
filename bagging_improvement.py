#!/usr/bin/env python3
"""
Titanic Dataset - Bagging Methods for Improved Accuracy
============================================================

This script implements various ensemble methods including:
- Random Forest Classifier
- Extra Trees Classifier  
- Bagging Classifier

All methods use hyperparameter tuning with GridSearchCV for optimal performance.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

def load_and_preprocess_data():
    """Load and preprocess the Titanic dataset."""
    print("Loading and preprocessing data...")
    
    # Load training data
    train_data = pd.read_csv('titanic/train.csv')
    
    # Handle missing values
    train_data = train_data.dropna(subset=['Age'])
    train_data = train_data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
    train_data['Embarked'] = train_data['Embarked'].fillna(train_data['Embarked'].mode()[0])
    
    # Encode categorical variables
    train_data = pd.get_dummies(train_data, columns=['Sex', 'Embarked'], drop_first=True)
    train_data['Age'] = train_data['Age'].astype(int)
    
    # Separate features and target
    X = train_data.drop(columns=['Survived'])
    y = train_data['Survived']
    
    return X, y

def train_random_forest(X_train, y_train, X_test, y_test):
    """Train Random Forest Classifier with hyperparameter tuning."""
    print("\n=== Random Forest Classifier ===")
    
    # Define parameter grid
    rf_param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 7, 10, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'criterion': ['gini', 'entropy']
    }
    
    # Grid search with cross-validation
    rf_grid_search = GridSearchCV(
        RandomForestClassifier(random_state=42),
        rf_param_grid,
        cv=5,
        n_jobs=-1,
        scoring='accuracy'
    )
    
    rf_grid_search.fit(X_train, y_train)
    
    # Get best model and predictions
    rf_best = rf_grid_search.best_estimator_
    y_pred_rf = rf_best.predict(X_test)
    rf_accuracy = accuracy_score(y_test, y_pred_rf)
    
    # Cross-validation score
    rf_cv_scores = cross_val_score(rf_best, X_train, y_train, cv=5)
    rf_cv_mean = rf_cv_scores.mean()
    rf_cv_std = rf_cv_scores.std()
    
    print(f"Best Random Forest parameters: {rf_grid_search.best_params_}")
    print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
    print(f"Random Forest CV Score: {rf_cv_mean:.4f} (+/- {rf_cv_std:.4f})")
    
    return rf_best, rf_accuracy, rf_cv_mean

def train_extra_trees(X_train, y_train, X_test, y_test):
    """Train Extra Trees Classifier with hyperparameter tuning."""
    print("\n=== Extra Trees Classifier ===")
    
    # Define parameter grid
    et_param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 7, 10, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'criterion': ['gini', 'entropy']
    }
    
    # Grid search with cross-validation
    et_grid_search = GridSearchCV(
        ExtraTreesClassifier(random_state=42),
        et_param_grid,
        cv=5,
        n_jobs=-1,
        scoring='accuracy'
    )
    
    et_grid_search.fit(X_train, y_train)
    
    # Get best model and predictions
    et_best = et_grid_search.best_estimator_
    y_pred_et = et_best.predict(X_test)
    et_accuracy = accuracy_score(y_test, y_pred_et)
    
    # Cross-validation score
    et_cv_scores = cross_val_score(et_best, X_train, y_train, cv=5)
    et_cv_mean = et_cv_scores.mean()
    et_cv_std = et_cv_scores.std()
    
    print(f"Best Extra Trees parameters: {et_grid_search.best_params_}")
    print(f"Extra Trees Accuracy: {et_accuracy:.4f}")
    print(f"Extra Trees CV Score: {et_cv_mean:.4f} (+/- {et_cv_std:.4f})")
    
    return et_best, et_accuracy, et_cv_mean

def train_bagging_classifier(X_train, y_train, X_test, y_test):
    """Train Bagging Classifier with hyperparameter tuning."""
    print("\n=== Bagging Classifier ===")
    
    # Base estimator
    base_dt = DecisionTreeClassifier(random_state=42)
    
    # Define parameter grid - FIXED: Changed base_estimator to estimator
    bag_param_grid = {
        'n_estimators': [10, 50, 100],
        'max_samples': [0.5, 0.7, 1.0],
        'max_features': [0.5, 0.7, 1.0]
    }
    
    # Grid search with cross-validation
    bag_grid_search = GridSearchCV(
        BaggingClassifier(estimator=base_dt, random_state=42),  # FIXED: estimator instead of base_estimator
        bag_param_grid,
        cv=5,
        n_jobs=-1,
        scoring='accuracy'
    )
    
    bag_grid_search.fit(X_train, y_train)
    
    # Get best model and predictions
    bag_best = bag_grid_search.best_estimator_
    y_pred_bag = bag_best.predict(X_test)
    bag_accuracy = accuracy_score(y_test, y_pred_bag)
    
    # Cross-validation score
    bag_cv_scores = cross_val_score(bag_best, X_train, y_train, cv=5)
    bag_cv_mean = bag_cv_scores.mean()
    bag_cv_std = bag_cv_scores.std()
    
    print(f"Best Bagging parameters: {bag_grid_search.best_params_}")
    print(f"Bagging Accuracy: {bag_accuracy:.4f}")
    print(f"Bagging CV Score: {bag_cv_mean:.4f} (+/- {bag_cv_std:.4f})")
    
    return bag_best, bag_accuracy, bag_cv_mean

def generate_submission(best_model, model_name):
    """Generate submission file using the best performing model."""
    print(f"\nGenerating submission with {model_name}...")
    
    # Load test data
    test_data = pd.read_csv('titanic/test.csv')
    passenger_ids = test_data['PassengerId']
    
    # Preprocess test data
    test_data = test_data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
    test_data['Age'] = test_data['Age'].fillna(test_data['Age'].mean())
    test_data['Fare'] = test_data['Fare'].fillna(test_data['Fare'].mean())
    test_data['Embarked'] = test_data['Embarked'].fillna(test_data['Embarked'].mode()[0])
    
    # Encode categorical variables
    test_data = pd.get_dummies(test_data, columns=['Sex', 'Embarked'], drop_first=True)
    test_data['Age'] = test_data['Age'].astype(int)
    
    # Make predictions
    predictions = best_model.predict(test_data)
    
    # Create submission DataFrame
    submission_df = pd.DataFrame({
        'PassengerId': passenger_ids,
        'Survived': predictions
    })
    
    # Save to CSV
    filename = f'submission_{model_name.lower().replace(" ", "_")}.csv'
    submission_df.to_csv(filename, index=False)
    print(f"Submission saved as {filename}")
    
    return submission_df

def compare_models(models_results):
    """Compare all models and return the best one."""
    print("\n" + "="*60)
    print("MODEL COMPARISON SUMMARY")
    print("="*60)
    
    best_model = None
    best_score = 0
    best_name = ""
    
    for name, (model, accuracy, cv_score) in models_results.items():
        print(f"{name:20s} | Accuracy: {accuracy:.4f} | CV Score: {cv_score:.4f}")
        
        if cv_score > best_score:
            best_score = cv_score
            best_model = model
            best_name = name
    
    print("="*60)
    print(f"BEST MODEL: {best_name} (CV Score: {best_score:.4f})")
    print("="*60)
    
    return best_model, best_name

def main():
    """Main function to run all ensemble methods."""
    print("Titanic Dataset - Bagging Methods for Improved Accuracy")
    print("=" * 60)
    
    # Load and preprocess data
    X, y = load_and_preprocess_data()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    
    # Train all models
    models_results = {}
    
    # Random Forest
    rf_best, rf_accuracy, rf_cv_mean = train_random_forest(X_train, y_train, X_test, y_test)
    models_results['Random Forest'] = (rf_best, rf_accuracy, rf_cv_mean)
    
    # Extra Trees
    et_best, et_accuracy, et_cv_mean = train_extra_trees(X_train, y_train, X_test, y_test)
    models_results['Extra Trees'] = (et_best, et_accuracy, et_cv_mean)
    
    # Bagging Classifier
    bag_best, bag_accuracy, bag_cv_mean = train_bagging_classifier(X_train, y_train, X_test, y_test)
    models_results['Bagging'] = (bag_best, bag_accuracy, bag_cv_mean)
    
    # Compare models and select best
    best_model, best_name = compare_models(models_results)
    
    # Generate submission with best model
    generate_submission(best_model, best_name)
    
    print(f"\nScript completed successfully!")
    print(f"Best model ({best_name}) submission generated.")

if __name__ == "__main__":
    main()