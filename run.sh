#!/bin/bash

echo "🚢 Starting Titanic Survival Predictor..."
echo "=================================================="

# Activate virtual environment
source titanic_env/bin/activate

# Start the Flask application
echo "Starting Flask application..."
echo "🌐 Open your browser and go to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the application"
echo "=================================================="

python app.py