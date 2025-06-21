#!/bin/bash

echo "🚢 Titanic Survival Predictor - Deployment Helper"
echo "================================================"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing git repository..."
    git init
    echo "✅ Git initialized"
else
    echo "✅ Git repository already exists"
fi

# Add all files
echo "📦 Adding files to git..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    # Commit changes
    echo "💾 Committing changes..."
    git commit -m "Prepare Titanic Survival Predictor for deployment

- Flask web application with machine learning model
- Beautiful UI with Bootstrap and Chart.js  
- Ready for deployment to Railway, Render, or other platforms
- Includes all deployment configuration files"
    echo "✅ Changes committed"
fi

echo ""
echo "🎯 Next Steps:"
echo ""
echo "1. Create a GitHub repository:"
echo "   - Go to https://github.com/new"
echo "   - Name it 'titanic-survival-predictor'"
echo "   - Keep it public"
echo "   - Don't initialize with README (we already have files)"
echo ""
echo "2. Connect and push to GitHub:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/titanic-survival-predictor.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy to Railway:"
echo "   - Go to https://railway.app"
echo "   - Sign up with GitHub"
echo "   - Click 'New Project' → 'Deploy from GitHub repo'"
echo "   - Select your repository"
echo "   - Your app will be live in minutes! 🎉"
echo ""
echo "📖 For detailed instructions, see DEPLOYMENT.md"
echo ""
echo "🌐 Your app will be accessible worldwide once deployed!"